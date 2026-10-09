"""Requirement Understanding Node (Jev)."""
from app.ai.gemini import classify_intent
from app.harness.state import AgentState

def requirement_understanding_node(state: AgentState) -> AgentState:
    intent = classify_intent(state.raw_input or "")
    state.history.append({"node": "requirement_understanding", "intent": intent})
    state.active_step = "extract_facts"
    return state
