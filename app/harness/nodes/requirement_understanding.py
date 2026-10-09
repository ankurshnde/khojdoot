"""
Requirement Understanding Node (Jev).
Classifies user intent (new business details vs conversational edits).
"""
from typing import Dict, Any
from app.ai.gemini import classify_intent
from app.harness.state import AgentState


def requirement_understanding_node(state: AgentState) -> Dict[str, Any]:
    text_to_analyze = state.get("edit_instruction") or state.get("raw_input") or ""
    intent = state.get("intent") or classify_intent(text_to_analyze)
    history = list(state.get("history") or [])
    history.append({"node": "requirement_understanding", "intent": intent})

    return {
        "intent": intent,
        "active_step": "extract_facts",
        "history": history,
    }
