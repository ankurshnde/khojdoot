"""
Agent Harness State Definition (LangGraph TypedDict State).
Owner: Ankur (Architecture Lead)
Contract: TRD v2.0 Section 6
"""
from typing import TypedDict, Optional, Dict, Any, List


class AgentState(TypedDict, total=False):
    """Canonical LangGraph State across the KhojDoot Agent Harness."""
    merchant_slug: str
    active_step: str
    raw_input: Optional[str]
    input_type: str  # text, voice, image
    intent: Optional[str]  # NEW_BUSINESS_INFO, EDIT_REQUEST, CLARIFICATION
    infobin: Optional[Dict[str, Any]]
    infobin_valid: bool
    is_complete: bool
    missing_fields: List[str]
    clarification_question: Optional[str]
    language: Optional[str]
    checkpoint1_approved: bool
    edit_instruction: Optional[str]
    website_spec: Optional[Dict[str, Any]]
    generated_html: Optional[str]
    validation_scorecard: Optional[Dict[str, Any]]
    checkpoint2_approved: bool
    published_url: Optional[str]
    error: Optional[str]
    history: List[Dict[str, Any]]
