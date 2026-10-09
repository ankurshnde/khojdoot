"""
WebsiteSpec JSON Schema.
Owner: Ankur / Gayatri
Contract: TRD v2.0 Section 10
"""
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional


class ThemeSpec(BaseModel):
    style: str = Field(default="traditional", description="minimal, editorial, traditional, premium")
    primary_color: str = "#E05A47"
    secondary_color: str = "#F8F5EE"
    font_family: str = "Noto Sans Devanagari, sans-serif"


class SectionSpec(BaseModel):
    id: str
    component: str  # hero, products, location, contact, footer
    enabled: bool = True
    title: Optional[str] = None
    props: Dict[str, Any] = Field(default_factory=dict)


class WebsiteSpec(BaseModel):
    slug: str
    version: int = 1
    theme: ThemeSpec = Field(default_factory=ThemeSpec)
    active_sections: List[SectionSpec] = Field(default_factory=list)
    status: str = "draft"
    validation_score: float = 0.0
