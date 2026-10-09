"""Information Extraction Node (Gemini)."""
from app.ai.gemini import extract_infobin_from_text
from app.harness.state import AgentState

def information_extraction_node(state: AgentState) -> AgentState:
    infobin = extract_infobin_from_text(state.raw_input or "")
    state.infobin = infobin.dict()
    state.active_step = "validate_infobin"
    return state
