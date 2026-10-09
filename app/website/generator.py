"""
Website Generator.
Owner: Gayatri / Ankur
Synthesizes components into full HTML according to WebsiteSpec.
Integrates Gayatri's 10 SME Design Systems Library with backward-compatible component fallback.
"""
from typing import Dict, Any
from app.website.components.hero import render_hero
from app.website.components.products import render_products
from app.website.components.location import render_location
from app.website.components.contact import render_contact
from app.website.components.footer import render_footer
from app.publishing.jsonld import generate_json_ld
from app.website.design_systems import DESIGN_SYSTEMS
from app.website.component_renderer import render_design_preview
from app.website.data_models import BusinessFacts, OfferingItem


def generate_website(spec: Dict[str, Any], infobin: Dict[str, Any]) -> str:
    name = infobin.get("name", "KhojDoot Merchant")
    phone = infobin.get("phone", "")
    location = infobin.get("location", "")
    services = infobin.get("services", "")
    hours = infobin.get("hours", "")
    menu = infobin.get("menu", [])

    theme = spec.get("theme", {})
    style_key = theme.get("style", "traditional")

    # Mapping from informal/harness themes to Gayatri's 10 Design Systems
    style_mapping = {
        "traditional": "home_kitchen",
        "पारंपारिक": "local_heritage",
        "heritage": "local_heritage",
        "minimal": "minimal_atelier",
        "साधा": "minimal_atelier",
        "modern": "modern_studio",
        "premium": "timeless_elegance",
        "रॉयल": "timeless_elegance",
        "market": "playful_market",
        "craft": "natural_craft",
        "artisan": "global_artisan",
        "pro": "neighborhood_pro",
        "boutique": "boutique_editorial",
    }

    selected_ds_key = style_mapping.get(style_key, style_key)

    # If the requested style matches one of the 10 Design Systems, render the rich design preview
    if selected_ds_key in DESIGN_SYSTEMS:
        ds = DESIGN_SYSTEMS[selected_ds_key]
        offerings = [
            OfferingItem(
                title=m.get("item", "Special Offering"),
                price=float(m["price"]) if str(m.get("price", "")).isdigit() else None,
                rate_unit="plate" if "थाळी" in m.get("item", "") else None,
            )
            for m in menu
        ]
        facts = BusinessFacts(
            name=name,
            phone=phone,
            city=location,
            story_bio=services,
            operating_hours=hours,
            offerings=offerings,
        )
        return render_design_preview(facts, ds)

    # Default fallback semantic HTML rendering
    primary_color = theme.get("primary_color", "#E05A47")
    font_family = theme.get("font_family", "Noto Sans Devanagari, sans-serif")
    json_ld = generate_json_ld(infobin)

    html_content = f"""<!DOCTYPE html>
<html lang="mr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name}</title>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body {{
            font-family: {font_family};
            margin: 0;
            padding: 0;
            background-color: #fafafa;
            color: #333;
            line-height: 1.6;
        }}
    </style>
    {json_ld}
</head>
<body>
    {render_hero(title=name, subtitle=services, phone=phone, theme_color=primary_color)}
    {render_products(items=menu)}
    {render_location(location=location, hours=hours)}
    {render_contact(phone=phone, name=name)}
    {render_footer(business_name=name)}
</body>
</html>
"""
    return html_content

