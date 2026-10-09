"""
Website Generator.
Owner: Gayatri / Ankur
Synthesizes components into full HTML according to WebsiteSpec.
"""
from typing import Dict, Any
from app.website.components.hero import render_hero
from app.website.components.products import render_products
from app.website.components.location import render_location
from app.website.components.contact import render_contact
from app.website.components.footer import render_footer
from app.publishing.jsonld import generate_json_ld


def generate_website(spec: Dict[str, Any], infobin: Dict[str, Any]) -> str:
    name = infobin.get("name", "KhojDoot Merchant")
    phone = infobin.get("phone", "")
    location = infobin.get("location", "")
    services = infobin.get("services", "")
    hours = infobin.get("hours", "")
    menu = infobin.get("menu", [])

    theme = spec.get("theme", {})
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
