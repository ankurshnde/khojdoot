"""WebsiteSpec Generation Node."""
from app.schemas.website_spec import WebsiteSpec, SectionSpec, ThemeSpec
from app.harness.state import AgentState

def spec_generation_node(state: AgentState) -> AgentState:
    sections = [
        SectionSpec(id="hero", component="hero"),
        SectionSpec(id="products", component="products"),
        SectionSpec(id="location", component="location"),
        SectionSpec(id="contact", component="contact"),
        SectionSpec(id="footer", component="footer"),
    ]
    spec = WebsiteSpec(
        slug=state.merchant_slug,
        theme=ThemeSpec(style="traditional"),
        active_sections=sections,
    )
    state.website_spec = spec.dict()
    state.active_step = "generate_code"
    return state
