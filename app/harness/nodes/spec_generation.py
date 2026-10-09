"""
WebsiteSpec Generation Node.
Translates approved InfoBin into WebsiteSpec presentation model.
"""
from typing import Dict, Any
from app.schemas.website_spec import WebsiteSpec, SectionSpec, ThemeSpec
from app.harness.state import AgentState


def spec_generation_node(state: AgentState) -> Dict[str, Any]:
    slug = state.get("merchant_slug", "merchant")
    sections = [
        SectionSpec(id="hero", component="hero"),
        SectionSpec(id="products", component="products"),
        SectionSpec(id="location", component="location"),
        SectionSpec(id="contact", component="contact"),
        SectionSpec(id="footer", component="footer"),
    ]
    spec = WebsiteSpec(
        slug=slug,
        theme=ThemeSpec(style="traditional"),
        active_sections=sections,
    )
    history = list(state.get("history") or [])
    history.append({"node": "spec_generation", "version": 1})

    return {
        "website_spec": spec.model_dump(),
        "active_step": "generate_code",
        "history": history,
    }
