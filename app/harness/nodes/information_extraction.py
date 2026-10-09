"""
Information Extraction Node (Gemini).
Extracts structured business entities into canonical InfoBin schema.
"""
from typing import Dict, Any
from app.ai.gemini import extract_infobin_from_text
from app.harness.state import AgentState


def information_extraction_node(state: AgentState) -> Dict[str, Any]:
    raw_input = state.get("raw_input") or ""
    infobin = extract_infobin_from_text(raw_input)
    history = list(state.get("history") or [])
    history.append({"node": "information_extraction", "shop_name": infobin.name})

    return {
        "infobin": infobin.model_dump(),
        "active_step": "validate_infobin",
        "history": history,
    }
