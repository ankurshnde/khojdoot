"""
LangGraph Orchestration Graph.
Owner: Ankur (Architecture Lead)
"""
from app.harness.state import AgentState
from app.harness.nodes.requirement_understanding import requirement_understanding_node
from app.harness.nodes.information_extraction import information_extraction_node
from app.harness.nodes.infobin_validation import infobin_validation_node
from app.harness.nodes.spec_generation import spec_generation_node
from app.harness.nodes.website_generation import website_generation_node
from app.harness.nodes.website_validation import website_validation_node


class WorkflowGraph:
    """Manages sequential execution of agent nodes."""
    def run_up_to_checkpoint1(self, state: AgentState) -> AgentState:
        state = requirement_understanding_node(state)
        state = information_extraction_node(state)
        state = infobin_validation_node(state)
        return state

    def run_checkpoint2(self, state: AgentState) -> AgentState:
        state = spec_generation_node(state)
        state = website_generation_node(state)
        state = website_validation_node(state)
        return state
