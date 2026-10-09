"""
Provenance Tracking Schema.
Owner: Ankur / Architecture
Contract: TRD v2.0 Section 8.2
"""
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class SourceType(str, Enum):
    USER_TEXT = "USER_TEXT"
    USER_VOICE = "USER_VOICE"
    USER_IMAGE = "USER_IMAGE"
    AI_INFERENCE = "AI_INFERENCE"
    USER_EDIT = "USER_EDIT"


class ProvenanceEntry(BaseModel):
    field_name: str
    source_type: SourceType
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    confirmed: bool = False
    notes: Optional[str] = None
