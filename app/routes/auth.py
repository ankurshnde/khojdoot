
import hashlib
import secrets
import re
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, Field

from app.db.connection import get_connection

router = APIRouter(prefix="/api/v1/auth", tags=["Authentication"])
bearer_scheme = HTTPBearer(auto_error=False)

OTP_TTL_MINUTES = 5
SESSION_TTL_DAYS = 7
MAX_OTP_ATTEMPTS = 5


def now():
    return datetime.now(timezone.utc)


def as_iso(value):
    return value.isoformat()


def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


class SendOTPRequest(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    mobile: str = Field(pattern=r"^[6-9]\d{9}$")


class VerifyOTPRequest(BaseModel):
    mobile: str = Field(pattern=r"^[6-9]\d{9}$")
    otp: str = Field(pattern=r"^\d{6}$")


@router.post("/send-otp")
def send_otp(payload: SendOTPRequest):
    name = payload.name.strip()

    if len(name) < 2:
        raise HTTPException(status_code=422, detail="Name must contain at least 2 characters")

    otp = f"{secrets.randbelow(1_000_000):06d}"
    timestamp = now()

    conn = get_connection()
    try:
        conn.execute(
            """
            INSERT INTO otp_verifications
                (phone, name, otp_hash, expires_at, attempts, created_at)
            VALUES (?, ?, ?, ?, 0, ?)
            ON CONFLICT(phone) DO UPDATE SET
                name = excluded.name,
                otp_hash = excluded.otp_hash,
                expires_at = excluded.expires_at,
                attempts = 0,
                created_at = excluded.created_at
            """,
            (
                payload.mobile,
                name,
                digest(otp),
                as_iso(timestamp + timedelta(minutes=OTP_TTL_MINUTES)),
                as_iso(timestamp),
            ),
        )
        conn.commit()
    finally:
        conn.close()

    # DEMO ONLY: Never return OTP in an API response in production.
    return {
        "message": "Demo OTP generated",
        "mobile": payload.mobile,
        "expires_in_seconds": OTP_TTL_MINUTES * 60,
        "demo_otp": otp,
    }


@router.post("/verify-otp")
def verify_otp(payload: VerifyOTPRequest):
    conn = get_connection()

    try:
        row = conn.execute(
            "SELECT * FROM otp_verifications WHERE phone = ?",
            (payload.mobile,),
        ).fetchone()

        if row is None:
            raise HTTPException(status_code=400, detail="Request a new OTP")

        if row["attempts"] >= MAX_OTP_ATTEMPTS:
            raise HTTPException(
                status_code=429,
                detail="Too many attempts. Request a new OTP.",
            )

        if now() >= datetime.fromisoformat(row["expires_at"]):
            conn.execute(
                "DELETE FROM otp_verifications WHERE phone = ?",
                (payload.mobile,),
            )
            conn.commit()
            raise HTTPException(status_code=400, detail="OTP expired. Request a new one.")

        if not secrets.compare_digest(row["otp_hash"], digest(payload.otp)):
            conn.execute(
                "UPDATE otp_verifications SET attempts = attempts + 1 WHERE phone = ?",
                (payload.mobile,),
            )
            conn.commit()
            raise HTTPException(status_code=400, detail="Invalid OTP")

        timestamp = now()

        conn.execute(
            """
            INSERT INTO users (name, phone, created_at)
            VALUES (?, ?, ?)
            ON CONFLICT(phone) DO UPDATE SET name = excluded.name
            """,
            (row["name"], payload.mobile, as_iso(timestamp)),
        )

        user = conn.execute(
            "SELECT id, name, phone FROM users WHERE phone = ?",
            (payload.mobile,),
        ).fetchone()

        token = secrets.token_urlsafe(32)

        conn.execute(
            """
            INSERT INTO auth_sessions (user_id, token_hash, expires_at, created_at)
            VALUES (?, ?, ?, ?)
            """,
            (
                user["id"],
                digest(token),
                as_iso(timestamp + timedelta(days=SESSION_TTL_DAYS)),
                as_iso(timestamp),
            ),
        )

        # OTP is single-use.
        conn.execute(
            "DELETE FROM otp_verifications WHERE phone = ?",
            (payload.mobile,),
        )
        conn.commit()

        return {
            "message": "Login successful",
            "access_token": token,
            "token_type": "bearer",
            "expires_in_seconds": SESSION_TTL_DAYS * 24 * 60 * 60,
            "user": {
                "id": user["id"],
                "name": user["name"],
                "mobile": user["phone"],
            },
        }
    finally:
        conn.close()


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
):
    if credentials is None:
        raise HTTPException(status_code=401, detail="Authentication required")

    conn = get_connection()
    try:
        row = conn.execute(
            """
            SELECT u.id, u.name, u.phone, s.expires_at
            FROM auth_sessions s
            JOIN users u ON u.id = s.user_id
            WHERE s.token_hash = ?
            """,
            (digest(credentials.credentials),),
        ).fetchone()

        if row is None:
            raise HTTPException(status_code=401, detail="Invalid session token")

        if now() >= datetime.fromisoformat(row["expires_at"]):
            conn.execute(
                "DELETE FROM auth_sessions WHERE token_hash = ?",
                (digest(credentials.credentials),),
            )
            conn.commit()
            raise HTTPException(status_code=401, detail="Session expired")

        return {
            "id": row["id"],
            "name": row["name"],
            "mobile": row["phone"],
        }
    finally:
        conn.close()


@router.get("/me")
def get_me(user=Depends(get_current_user)):
    return {"authenticated": True, "user": user}
