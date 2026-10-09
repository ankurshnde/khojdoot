"""
Canonical InfoBin Schema.
Owner: Ankur / Architecture
Contract: TRD v2.0 Section 8.1
"""
from pydantic import BaseModel, Field
from typing import List, Optional


class MenuItem(BaseModel):
    item: str = Field(..., description="Name of the food item or service product")
    price: Optional[float] = Field(None, description="Price in INR")


class InfoBin(BaseModel):
    name: str = Field(..., description="Business name")
    category: str = Field(default="general", description="Business category (e.g. food, retail, service)")
    location: str = Field(default="", description="Address / city / neighborhood")
    phone: str = Field(default="", description="Contact phone / WhatsApp number")
    services: Optional[str] = Field(default="", description="Short description of offerings")
    menu: List[MenuItem] = Field(default_factory=list, description="List of items or products with pricing")
    hours: Optional[str] = Field(default="", description="Operating hours")
    language: Optional[str] = Field(default="mr-IN", description="Preferred regional language code")
