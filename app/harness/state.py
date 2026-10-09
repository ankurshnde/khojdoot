"""
Agent Harness State Definition.
Owner: Ankur (Architecture Lead)
"""
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field


class AgentState(BaseModel):
    merchant_slug: str
    active_step: str = "understand_requirement"
    raw_input: Optional[str] = None
    input_type: str = "text"  # text, voice, image
    infobin: Optional[Dict[str, Any]] = None
    infobin_valid: bool = False
    checkpoint1_approved: bool = False
    website_spec: Optional[Dict[str, Any]] = None
    generated_html: Optional[str] = None
    validation_scorecard: Optional[Dict[str, Any]] = None
    checkpoint2_approved: bool = False
    history: List[Dict[str, Any]] = Field(default_factory=list)
