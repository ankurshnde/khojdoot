"""
Checkpoint 1: Approval Gate Node.
Marks active step as await_approval for user review in Web Chat.
"""
from typing import Dict, Any
from app.harness.state import AgentState


def approval_node(state: AgentState) -> Dict[str, Any]:
    history = list(state.get("history") or [])
    history.append({"node": "approval", "checkpoint": "CHECKPOINT_1_AWAITING_APPROVAL"})

    return {
        "active_step": "await_approval",
        "history": history,
    }
