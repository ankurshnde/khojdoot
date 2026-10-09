"""
LangGraph Orchestration Graph (True LangGraph StateGraph Engine).
Owner: Ankur (Architecture Lead)
Implements: TRD v2.0 Section 6 LangGraph DAG with Two Checkpoint Gates & Cyclic Edits.
"""
from typing import Dict, Any, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from app.harness.state import AgentState
from app.harness.nodes.requirement_understanding import requirement_understanding_node
from app.harness.nodes.information_extraction import information_extraction_node
from app.harness.nodes.infobin_validation import infobin_validation_node
from app.harness.nodes.approval import approval_node
from app.harness.nodes.spec_generation import spec_generation_node
from app.harness.nodes.website_generation import website_generation_node
from app.harness.nodes.website_validation import website_validation_node
from app.harness.nodes.patch_spec import patch_spec_node


def route_after_understanding(state: AgentState) -> Literal["patch_spec", "generate_spec", "extract_facts"]:
    """
    Branching logic after requirement understanding:
    1. If user requested a natural language edit on an existing spec -> patch_spec
    2. If merchant already approved Checkpoint 1 -> generate_spec
    3. Otherwise -> extract new facts from raw input
    """
    if state.get("intent") == "EDIT_REQUEST" and state.get("website_spec"):
        return "patch_spec"
    if state.get("checkpoint1_approved", False) and state.get("infobin"):
        return "generate_spec"
    return "extract_facts"


def route_after_validation(state: AgentState) -> Literal["approval", "__end__"]:
    """Routes based on InfoBin validity. If valid, pauses at Checkpoint 1 (approval node)."""
    if not state.get("infobin_valid", False):
        return "__end__"
    return "approval"


def build_harness_graph() -> StateGraph:
    """Builds the canonical LangGraph StateGraph for the KhojDoot Agent Harness."""
    builder = StateGraph(AgentState)

    # 1. Add all nodes
    builder.add_node("understand_requirement", requirement_understanding_node)
    builder.add_node("extract_facts", information_extraction_node)
    builder.add_node("validate_infobin", infobin_validation_node)
    builder.add_node("approval", approval_node)
    builder.add_node("generate_spec", spec_generation_node)
    builder.add_node("generate_website", website_generation_node)
    builder.add_node("validate_website", website_validation_node)
    builder.add_node("patch_spec", patch_spec_node)

    # 2. Add edges & conditional branching
    builder.add_edge(START, "understand_requirement")

    builder.add_conditional_edges(
        "understand_requirement",
        route_after_understanding,
        {
            "patch_spec": "patch_spec",
            "generate_spec": "generate_spec",
            "extract_facts": "extract_facts",
        },
    )

    builder.add_edge("extract_facts", "validate_infobin")

    builder.add_conditional_edges(
        "validate_infobin",
        route_after_validation,
        {
            "approval": "approval",
            "__end__": END,
        },
    )

    # Checkpoint 1 gate: pauses at approval node
    builder.add_edge("approval", END)

    # Checkpoint 2 pipeline: spec -> website -> validation -> preview
    builder.add_edge("generate_spec", "generate_website")
    builder.add_edge("generate_website", "validate_website")
    builder.add_edge("validate_website", END)

    # Checkpoint 2 cyclic edit loop: patch_spec -> generate_website -> validate_website -> END
    builder.add_edge("patch_spec", "generate_website")

    return builder


# Global in-memory checkpointer preserving state across HTTP requests
checkpointer = MemorySaver()

# Compiled graph ready for execution
compiled_harness_graph = build_harness_graph().compile(checkpointer=checkpointer)
