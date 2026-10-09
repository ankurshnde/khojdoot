"""
Website Validation Node.
Executes the 8-point deterministic website validation suite.
"""
from typing import Dict, Any
from app.validation.website import validate_website_html
from app.harness.state import AgentState


def website_validation_node(state: AgentState) -> Dict[str, Any]:
    html = state.get("generated_html") or ""
    scorecard = validate_website_html(html)

    history = list(state.get("history") or [])
    history.append({
        "node": "website_validation",
        "passed": scorecard.get("passed", False),
        "summary": scorecard.get("summary", ""),
    })

    return {
        "validation_scorecard": scorecard,
        "active_step": "await_preview_edit",
        "history": history,
    }
