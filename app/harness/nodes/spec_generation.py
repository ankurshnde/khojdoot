"""
WebsiteSpec Generation Node.
Translates approved InfoBin into WebsiteSpec presentation model.
"""
from typing import Dict, Any
from app.schemas.website_spec import WebsiteSpec, SectionSpec, ThemeSpec
from app.harness.state import AgentState


def spec_generation_node(state: AgentState) -> Dict[str, Any]:
    slug = state.get("merchant_slug", "merchant")
    infobin = state.get("infobin") or {}

    category = (infobin.get("category") or "").lower()
    explicit_style = infobin.get("style")

    # Smart mapping of SME categories to Gayatri's 10 Design Systems & DESIGN.md
    if explicit_style:
        chosen_style = explicit_style
    elif any(k in category for k in ["auto", "garage", "repair", "service", "mechanic", "bike", "car"]):
        chosen_style = "neighborhood_pro"
    elif any(k in category for k in ["fashion", "clothing", "boutique", "saree", "textile", "cotton"]):
        chosen_style = "boutique_editorial"
    elif any(k in category for k in ["craft", "pottery", "handicraft", "artisan", "माती", "कला"]):
        chosen_style = "natural_craft"
    elif any(k in category for k in ["chai", "tea", "cafe", "sweet", "mithai", "चाय", "नाश्ता"]):
        chosen_style = "local_heritage"
    elif any(k in category for k in ["breakfast", "tiffin_center", "market", "grocery", "kirana", "టిఫిన్"]):
        chosen_style = "playful_market"
    elif any(k in category for k in ["dairy", "organic", "luxury", "ghee", "दूध", "जैविक"]):
        chosen_style = "timeless_elegance"
    else:
        chosen_style = "home_kitchen"

    sections = [
        SectionSpec(id="hero", component="hero"),
        SectionSpec(id="products", component="products"),
        SectionSpec(id="location", component="location"),
        SectionSpec(id="contact", component="contact"),
        SectionSpec(id="footer", component="footer"),
    ]
    spec = WebsiteSpec(
        slug=slug,
        theme=ThemeSpec(style=chosen_style),
        active_sections=sections,
    )
    history = list(state.get("history") or [])
    history.append({"node": "spec_generation", "version": 1})

    return {
        "website_spec": spec.model_dump(),
        "active_step": "generate_code",
        "history": history,
    }
