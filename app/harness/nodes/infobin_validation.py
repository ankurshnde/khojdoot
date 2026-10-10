"""
InfoBin Validation Node.
Performs deterministic validation on extracted business information.
"""
from typing import Dict, Any
from app.schemas.infobin import InfoBin
from app.validation.business import validate_infobin
from app.harness.state import AgentState


def infobin_validation_node(state: AgentState) -> Dict[str, Any]:
    infobin_data = state.get("infobin")
    missing_fields = state.get("missing_fields") or []
    valid = False
    validation_report = {}

    if infobin_data:
        validation_report = validate_infobin(InfoBin(**infobin_data))
        valid = validation_report.get("valid", False) and (len(missing_fields) == 0)

    history = list(state.get("history") or [])
    history.append({
        "node": "infobin_validation",
        "valid": valid,
        "missing_fields": missing_fields,
        "score": validation_report.get("score", 0.0),
    })

    return {
        "infobin_valid": valid,
        "active_step": "await_approval" if valid else "need_clarification",
        "history": history,
    }

