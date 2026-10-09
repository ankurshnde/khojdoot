"""Website Generation Node."""
from app.website.generator import generate_website
from app.harness.state import AgentState

def website_generation_node(state: AgentState) -> AgentState:
    if state.website_spec and state.infobin:
        html = generate_website(state.website_spec, state.infobin)
        state.generated_html = html
    state.active_step = "validate_website"
    return state
