"""InfoBin Validation Node."""
from app.schemas.infobin import InfoBin
from app.validation.business import validate_infobin
from app.harness.state import AgentState

def infobin_validation_node(state: AgentState) -> AgentState:
    if state.infobin:
        result = validate_infobin(InfoBin(**state.infobin))
        state.infobin_valid = result["valid"]
    state.active_step = "await_approval"
    return state
