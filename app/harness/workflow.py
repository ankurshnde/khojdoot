"""
Workflow & Control Logic Interface.
Owner: Ankur (Architecture Lead)
Contract with Abhishek: harness.execute_workflow(request_context)
"""
from typing import Dict, Any
from app.harness.state import AgentState
from app.harness.graph import WorkflowGraph

graph = WorkflowGraph()


def execute_workflow(request_context: Dict[str, Any]) -> Dict[str, Any]:
    slug = request_context.get("slug", "default-merchant")
    raw_input = request_context.get("raw_input", "")
    phase = request_context.get("phase", "checkpoint1")

    state = AgentState(merchant_slug=slug, raw_input=raw_input)

    if phase == "checkpoint1":
        state = graph.run_up_to_checkpoint1(state)
    elif phase == "checkpoint2":
        state = graph.run_checkpoint2(state)

    return state.dict()
