"""Checkpoint 1 Approval Node."""
from app.harness.state import AgentState

def approval_node(state: AgentState) -> AgentState:
    state.active_step = "generate_spec"
    return state
