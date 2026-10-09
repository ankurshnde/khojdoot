"""
Authentication & Dummy OTP Module.
User ID is the merchant's mobile number.
Endpoints: Send OTP, Verify OTP, Auth Status.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Dict
from datetime import datetime, timedelta
import random

router = APIRouter()

# In-memory store for active demo OTPs: {mobile: {"otp": "...", "expires_at": datetime}}
OTP_STORE: Dict[str, Dict] = {}

# Default master OTP for seamless hackathon testing/demoing
DEMO_MASTER_OTP = "123456"


class SendOTPRequest(BaseModel):
    mobile: str = Field(..., description="10-digit mobile number or with country code")


class VerifyOTPRequest(BaseModel):
    mobile: str = Field(..., description="User ID / Mobile number")
    otp: str = Field(..., description="6-digit OTP code")


class AuthResponse(BaseModel):
    status: str
    message: str
    user_id: Optional[str] = None
    access_token: Optional[str] = None


def normalize_mobile(mobile: str) -> str:
    """Cleans phone numbers into a consistent 10-digit format."""
    clean = mobile.replace("+91", "").replace("-", "").replace(" ", "").strip()
    if clean.startswith("0"):
        clean = clean[1:]
    return clean


@router.post("/send-otp", response_model=Dict)
def send_otp(request: SendOTPRequest):
    """
    Generates and sends a dummy OTP to the merchant's mobile number.
    For hackathon demo convenience, OTP is also returned in the response and defaults to '123456'.
    """
    phone = normalize_mobile(request.mobile)
    if len(phone) < 10:
        raise HTTPException(status_code=400, detail="Invalid mobile number. Must be at least 10 digits.")

    # Generate a 6-digit OTP (or use DEMO_MASTER_OTP)
    generated_otp = str(random.randint(100000, 999999))
    expires_at = datetime.utcnow() + timedelta(minutes=10)

    OTP_STORE[phone] = {
        "otp": generated_otp,
        "expires_at": expires_at,
    }

    return {
        "status": "success",
        "message": f"OTP sent to {request.mobile}",
        "user_id": phone,
        "demo_otp": generated_otp,
        "master_demo_otp": DEMO_MASTER_OTP,
        "expires_in_seconds": 600,
    }


@router.post("/verify-otp", response_model=AuthResponse)
def verify_otp(request: VerifyOTPRequest):
    """
    Verifies the submitted OTP against the mobile number.
    Accepts either the generated OTP or the master demo OTP ('123456').
    """
    phone = normalize_mobile(request.mobile)
    submitted_otp = request.otp.strip()

    # Allow master demo OTP for instant evaluation without checking state
    if submitted_otp == DEMO_MASTER_OTP:
        return AuthResponse(
            status="authenticated",
            message="OTP verified successfully (Master Demo OTP).",
            user_id=phone,
            access_token=f"khojdoot_token_{phone}_{int(datetime.utcnow().timestamp())}",
        )

    # Check generated OTP
    record = OTP_STORE.get(phone)
    if not record:
        raise HTTPException(status_code=400, detail="No OTP requested for this mobile number. Please send OTP first.")

    if datetime.utcnow() > record["expires_at"]:
        OTP_STORE.pop(phone, None)
        raise HTTPException(status_code=400, detail="OTP has expired. Please request a new one.")

    if record["otp"] != submitted_otp:
        raise HTTPException(status_code=400, detail="Invalid OTP code entered.")

    # Successful verification
    OTP_STORE.pop(phone, None)
    return AuthResponse(
        status="authenticated",
        message="OTP verified successfully.",
        user_id=phone,
        access_token=f"khojdoot_token_{phone}_{int(datetime.utcnow().timestamp())}",
    )


@router.get("/status/{mobile}")
def check_auth_status(mobile: str):
    """Checks whether an active OTP request exists for this user ID (mobile)."""
    phone = normalize_mobile(mobile)
    has_pending = phone in OTP_STORE and datetime.utcnow() <= OTP_STORE[phone]["expires_at"]
    return {
        "user_id": phone,
        "has_pending_otp": has_pending,
    }
