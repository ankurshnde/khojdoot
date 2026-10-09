"""Website Validation Node."""
from app.validation.website import validate_website_html
from app.harness.state import AgentState

def website_validation_node(state: AgentState) -> AgentState:
    if state.generated_html:
        res = validate_website_html(state.generated_html)
        state.validation_scorecard = res
    state.active_step = "await_preview_edit"
    return state
