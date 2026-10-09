"""
Website Generation Node.
Synthesizes bounded components into full HTML according to WebsiteSpec.
"""
from typing import Dict, Any
from app.website.generator import generate_website
from app.harness.state import AgentState


def website_generation_node(state: AgentState) -> Dict[str, Any]:
    spec = state.get("website_spec") or {}
    infobin = state.get("infobin") or {}
    html = generate_website(spec, infobin)

    history = list(state.get("history") or [])
    history.append({"node": "website_generation", "bytes": len(html)})

    return {
        "generated_html": html,
        "active_step": "validate_website",
        "history": history,
    }
