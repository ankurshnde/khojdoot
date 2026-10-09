"""
Database CRUD Helpers.
Owner: Shantanu (Database / Persistence)
"""
import json
from datetime import datetime
from typing import Optional, Dict, Any, List
from app.db.database import get_connection


def create_or_update_shop(sme_id: str, slug: str, name: str, phone: str = "", city: str = "") -> int:
    conn = get_connection()
    cursor = conn.cursor()
    now = datetime.utcnow().isoformat()

    shop = cursor.execute("SELECT id FROM shops WHERE slug = ?", (slug,)).fetchone()
    if shop:
        cursor.execute(
            "UPDATE shops SET sme_id = ?, name = ?, phone = ?, city = ?, updated_at = ? WHERE id = ?",
            (sme_id, name, phone, city, now, shop["id"]),
        )
        shop_id = shop["id"]
    else:
        cursor.execute(
            "INSERT INTO shops (sme_id, slug, name, phone, city, status, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (sme_id, slug, name, phone, city, "draft", now, now),
        )
        shop_id = cursor.lastrowid

    conn.commit()
    conn.close()
    return shop_id


def get_shop_by_slug(slug: str) -> Optional[Dict[str, Any]]:
    conn = get_connection()
    row = conn.execute("SELECT * FROM shops WHERE slug = ?", (slug,)).fetchone()
    conn.close()
    return dict(row) if row else None


def save_bin(shop_id: int, bin_type: str, data: Dict[str, Any]):
    conn = get_connection()
    conn.execute(
        "INSERT INTO bins (shop_id, bin_type, data) VALUES (?, ?, ?)",
        (shop_id, bin_type, json.dumps(data, ensure_ascii=False)),
    )
    conn.commit()
    conn.close()


def get_bin(shop_id: int, bin_type: str) -> Optional[Dict[str, Any]]:
    conn = get_connection()
    row = conn.execute(
        "SELECT data FROM bins WHERE shop_id = ? AND bin_type = ? ORDER BY id DESC LIMIT 1",
        (shop_id, bin_type),
    ).fetchone()
    conn.close()
    return json.loads(row["data"]) if row else None


def save_provenance(shop_id: int, field_name: str, source_type: str, confidence: float = 1.0, confirmed: int = 0):
    conn = get_connection()
    conn.execute(
        "INSERT INTO provenance (shop_id, field_name, source_type, confidence, confirmed) VALUES (?, ?, ?, ?, ?)",
        (shop_id, field_name, source_type, confidence, confirmed),
    )
    conn.commit()
    conn.close()


def save_consent(shop_id: int, consent_type: str, payload_hash: str = ""):
    conn = get_connection()
    now = datetime.utcnow().isoformat()
    conn.execute(
        "INSERT INTO consent_records (shop_id, consent_type, approved_at, payload_hash) VALUES (?, ?, ?, ?)",
        (shop_id, consent_type, now, payload_hash),
    )
    conn.commit()
    conn.close()


def save_website_spec(shop_id: int, version: int, spec_data: Dict[str, Any], validation_score: float = 0.0, status: str = "generated"):
    conn = get_connection()
    conn.execute(
        "INSERT INTO website_specs (shop_id, version, spec_data, validation_score, status) VALUES (?, ?, ?, ?, ?)",
        (shop_id, version, json.dumps(spec_data, ensure_ascii=False), validation_score, status),
    )
    conn.commit()
    conn.close()


def get_latest_website_spec(shop_id: int) -> Optional[Dict[str, Any]]:
    conn = get_connection()
    row = conn.execute(
        "SELECT spec_data FROM website_specs WHERE shop_id = ? ORDER BY version DESC LIMIT 1",
        (shop_id,),
    ).fetchone()
    conn.close()
    return json.loads(row["spec_data"]) if row else None
