"""
Data Models for Persistence Layer.
Owner: Shantanu (Database / Persistence)
"""
from pydantic import BaseModel
from typing import Optional, Any, Dict


class ShopRecord(BaseModel):
    id: Optional[int] = None
    sme_id: Optional[str] = None
    slug: str
    name: str
    phone: Optional[str] = None
    city: Optional[str] = None
    status: Optional[str] = "draft"
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class BinRecord(BaseModel):
    id: Optional[int] = None
    shop_id: int
    bin_type: str
    data: Dict[str, Any]


class ProvenanceRecord(BaseModel):
    id: Optional[int] = None
    shop_id: int
    field_name: str
    source_type: str
    confidence: Optional[float] = 1.0
    confirmed: Optional[int] = 0


class ConsentRecord(BaseModel):
    id: Optional[int] = None
    shop_id: int
    consent_type: str
    approved_at: str
    payload_hash: Optional[str] = None


class WebsiteSpecRecord(BaseModel):
    id: Optional[int] = None
    shop_id: int
    version: int = 1
    spec_data: Dict[str, Any]
    validation_score: float = 0.0
    status: str = "generated"
