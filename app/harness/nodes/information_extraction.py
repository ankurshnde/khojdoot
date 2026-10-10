"""
Information Extraction Node (Gemini).
Extracts structured business entities into canonical InfoBin schema and reasons over missing fields.
"""
from typing import Dict, Any
from app.ai.gemini import extract_and_reason_business_schema
from app.harness.state import AgentState


def information_extraction_node(state: AgentState) -> Dict[str, Any]:
    raw_input = state.get("raw_input") or ""
    existing_infobin = state.get("infobin")
    language_hint = state.get("language")

    reasoning_result = extract_and_reason_business_schema(
        raw_input,
        existing_infobin=existing_infobin,
        language_hint=language_hint,
    )

    infobin_data = reasoning_result.get("infobin") or {}
    is_complete = reasoning_result.get("is_complete", False)
    missing_fields = reasoning_result.get("missing_fields", [])
    clarification_question = reasoning_result.get("clarification_question", "")

    history = list(state.get("history") or [])
    history.append({
        "node": "information_extraction",
        "shop_name": infobin_data.get("name"),
        "is_complete": is_complete,
        "missing_fields": missing_fields,
    })

    return {
        "infobin": infobin_data,
        "is_complete": is_complete,
        "missing_fields": missing_fields,
        "clarification_question": clarification_question,
        "active_step": "validate_infobin",
        "history": history,
    }

