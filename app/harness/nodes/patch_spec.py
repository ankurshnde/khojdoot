"""
WebsiteSpec Patching Node (Checkpoint 2 Natural-Language Edit Loop).
Applies conversational changes to the presentation model and prepares re-generation.
"""
from typing import Dict, Any
from app.website.patcher import patch_website_spec
from app.harness.state import AgentState


def patch_spec_node(state: AgentState) -> Dict[str, Any]:
    current_spec = state.get("website_spec") or {"theme": {"style": "traditional"}, "version": 1}
    instruction = state.get("edit_instruction") or state.get("raw_input") or ""

    patched = patch_website_spec(current_spec, instruction)

    history = list(state.get("history") or [])
    history.append({
        "node": "patch_spec",
        "instruction": instruction,
        "new_version": patched.get("version", 2),
    })

    return {
        "website_spec": patched,
        "active_step": "generate_code",
        "history": history,
    }
