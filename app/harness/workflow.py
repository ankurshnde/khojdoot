"""
Workflow & Control Logic Interface (LangGraph Execution Harness).
Owner: Ankur (Architecture Lead)
Contract with Abhishek: harness.execute_workflow(request_context)
"""
from typing import Dict, Any, Optional
from app.harness.state import AgentState
from app.harness.graph import compiled_harness_graph


def execute_workflow(request_context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Executes the LangGraph Agent Harness pipeline for a given merchant request.
    Maintains persistent thread memory across turns via thread_id.
    """
    slug = request_context.get("slug", "default-merchant")
    raw_input = request_context.get("raw_input", "")
    phase = request_context.get("phase", "checkpoint1")
    edit_instruction = request_context.get("edit_instruction")
    approved = request_context.get("approved", False)

    config = {"configurable": {"thread_id": slug}}

    # Initial state payload
    state_input: AgentState = {
        "merchant_slug": slug,
        "raw_input": raw_input,
        "input_type": request_context.get("input_type", "text"),
        "checkpoint1_approved": approved or (phase == "checkpoint2"),
        "edit_instruction": edit_instruction,
    }

    if edit_instruction:
        state_input["intent"] = "EDIT_REQUEST"
    if request_context.get("infobin"):
        state_input["infobin"] = request_context["infobin"]
    if request_context.get("language"):
        state_input["language"] = request_context["language"]

    # Invoke the compiled LangGraph StateGraph
    final_state = compiled_harness_graph.invoke(state_input, config=config)

    return dict(final_state)


def get_workflow_state(slug: str) -> Optional[Dict[str, Any]]:
    """Retrieves current checkpointed state for a given merchant thread."""
    config = {"configurable": {"thread_id": slug}}
    state_snapshot = compiled_harness_graph.get_state(config)
    if state_snapshot and state_snapshot.values:
        return dict(state_snapshot.values)
    return None
