"""Website Generator.
Adheres strictly to docs/DESIGN.md & app/website/components architecture.
Synthesizes bounded components into full, crawlable Indic MSME websites.
"""
from typing import Dict, Any, List
from app.website.components.hero import render_hero
from app.website.components.products import render_products
from app.website.components.location import render_location
from app.website.components.contact import render_contact
from app.website.components.footer import render_footer
from app.website.components.fab import render_fab
from app.publishing.jsonld import generate_json_ld


# Themes directly defined in docs/DESIGN.md Section 2 with Indic MSME palettes
DESIGN_MD_THEMES: Dict[str, Dict[str, Any]] = {
    "traditional": {
        "id": "traditional",
        "name": "Traditional / Marathi Rasoi",
        "primary": "#C84B31",       # Deep Terracotta / Kesari
        "secondary": "#2D4059",     # Slate Navy
        "background": "#FAF8F5",    # Warm Cream
        "surface": "#FFFFFF",
        "text": "#1F2937",          # Charcoal
        "font_family": "'Noto Sans Devanagari', 'Poppins', sans-serif",
    },
    "home_kitchen": {
        "id": "home_kitchen",
        "name": "Traditional Home Rasoi",
        "primary": "#C84B31",       # Deep Terracotta
        "secondary": "#78350F",     # Warm Brown
        "background": "#FAF8F5",    # Warm Cream
        "surface": "#FFFFFF",
        "text": "#1F2937",
        "font_family": "'Noto Sans Devanagari', 'Poppins', sans-serif",
    },
    "minimal": {
        "id": "minimal",
        "name": "Modern Fresh / Groceries & Kirana",
        "primary": "#16A34A",       # Fresh Green
        "secondary": "#0F172A",     # Deep Slate
        "background": "#F8FAFC",    # Cool Off-White
        "surface": "#FFFFFF",
        "text": "#0F172A",
        "font_family": "'Noto Sans Devanagari', 'Noto Sans Telugu', 'Poppins', sans-serif",
    },
    "playful_market": {
        "id": "playful_market",
        "name": "Playful Market Tiffins",
        "primary": "#E65100",       # Turmeric Orange
        "secondary": "#2E7D32",     # Chili Leaf Green
        "background": "#FFFDF7",    # Warm Off-White
        "surface": "#FFFFFF",
        "text": "#1C1917",
        "font_family": "'Noto Sans Telugu', 'Poppins', sans-serif",
    },
    "premium": {
        "id": "premium",
        "name": "Royal / Premium Services",
        "primary": "#D4AF37",       # Warm Gold
        "secondary": "#1E1B4B",     # Midnight Indigo
        "background": "#0B0F19",    # Dark Luxury
        "surface": "#161F30",
        "text": "#F3F4F6",
        "font_family": "'Cinzel', 'Noto Sans Devanagari', serif",
    },
    "timeless_elegance": {
        "id": "timeless_elegance",
        "name": "Timeless Elegance & Farm Purity",
        "primary": "#14532D",       # Forest Emerald
        "secondary": "#D4AF37",     # Antique Gold
        "background": "#F7FBF8",    # Cream Ivory
        "surface": "#FFFFFF",
        "text": "#132A1C",
        "font_family": "'Lora', 'Noto Sans Devanagari', serif",
    },
    "local_heritage": {
        "id": "local_heritage",
        "name": "Local Heritage Chai & Cafe",
        "primary": "#D97706",       # Deep Saffron / Amber
        "secondary": "#78350F",     # Warm Coffee Roast
        "background": "#FFFBEB",    # Chai Cream
        "surface": "#FFFFFF",
        "text": "#451A03",
        "font_family": "'Noto Sans Devanagari', 'Poppins', sans-serif",
    },
    "boutique_editorial": {
        "id": "boutique_editorial",
        "name": "Boutique Editorial & Fashion",
        "primary": "#831843",       # Mulberry Rose
        "secondary": "#FCE7F3",     # Soft Rose Mist
        "background": "#FFFDFD",
        "surface": "#FFFFFF",
        "text": "#371B26",
        "font_family": "'Playfair Display', 'Noto Sans Telugu', serif",
    },
    "natural_craft": {
        "id": "natural_craft",
        "name": "Natural Craft & Terracotta Pottery",
        "primary": "#9C4124",       # Raw Clay Terracotta
        "secondary": "#E8C99B",     # Ochre Clay
        "background": "#FAF5EF",
        "surface": "#FFFFFF",
        "text": "#2C1A14",
        "font_family": "'Merriweather', 'Noto Sans Devanagari', serif",
    },
    "neighborhood_pro": {
        "id": "neighborhood_pro",
        "name": "Neighborhood Pro & Precision Services",
        "primary": "#1E3A8A",       # Industrial Blue
        "secondary": "#F59E0B",     # Safety Amber
        "background": "#F1F5F9",
        "surface": "#FFFFFF",
        "text": "#0F172A",
        "font_family": "'Inter', 'Noto Sans Telugu', sans-serif",
    },
}


def generate_website(spec: Dict[str, Any], infobin: Dict[str, Any]) -> str:
    """Synthesizes modular components into a complete, crawlable HTML page.
    Adheres strictly to docs/DESIGN.md & app/website/components architecture.
    """
    name = infobin.get("name", "KhojDoot Merchant")
    phone = infobin.get("phone", "")
    location = infobin.get("location", "")
    services = infobin.get("services", "")
    hours = infobin.get("hours", "")
    menu = infobin.get("menu", [])
    language = infobin.get("language") or "mr-IN"

    # Resolve theme tokens from docs/DESIGN.md
    theme_spec = spec.get("theme", {})
    style_key = theme_spec.get("style", "traditional")

    theme_tokens = DESIGN_MD_THEMES.get(style_key)
    if not theme_tokens:
        # Check aliases
        if style_key in ["पारंपारिक", "heritage"]:
            theme_tokens = DESIGN_MD_THEMES["local_heritage"]
        elif style_key in ["साधा", "fresh"]:
            theme_tokens = DESIGN_MD_THEMES["minimal"]
        elif style_key in ["रॉयल", "gold"]:
            theme_tokens = DESIGN_MD_THEMES["timeless_elegance"]
        else:
            theme_tokens = DESIGN_MD_THEMES["traditional"]

    # Allow custom color override if explicitly present in spec
    if theme_spec.get("primary_color"):
        theme_tokens = dict(theme_tokens)
        theme_tokens["primary"] = theme_spec["primary_color"]

    bg_color = theme_tokens["background"]
    text_color = theme_tokens["text"]
    font_family = theme_tokens["font_family"]

    # Language tag for HTML root
    lang_short = "mr"
    if "te" in language:
        lang_short = "te"
    elif "hi" in language:
        lang_short = "hi"
    elif "en" in language:
        lang_short = "en"

    json_ld = generate_json_ld(infobin)

    # Synthesize all components from app/website/components
    hero_html = render_hero(title=name, subtitle=services, phone=phone, theme=theme_tokens, language=language)
    products_html = render_products(items=menu, theme=theme_tokens, language=language)
    location_html = render_location(location=location, hours=hours, theme=theme_tokens, language=language)
    contact_html = render_contact(phone=phone, name=name, theme=theme_tokens, language=language)
    footer_html = render_footer(business_name=name, theme=theme_tokens)
    fab_html = render_fab(phone=phone, name=name, theme=theme_tokens, language=language)

    html_content = f"""<!DOCTYPE html>
<html lang="{lang_short}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} — Official Website</title>
    <meta name="description" content="{name}: {services} in {location}. Call or WhatsApp {phone}.">

    <!-- Fonts mandated by docs/DESIGN.md Section 1 -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Lora:ital,wght@0,500;0,700;1,400&family=Merriweather:wght@400;700&family=Noto+Sans+Devanagari:wght@400;600;700;800&family=Noto+Sans+Telugu:wght@400;600;700;800&family=Playfair+Display:wght@600;700&family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">

    <!-- Structured JSON-LD Data for Web & LLM Crawlers (docs/DESIGN.md Section 4) -->
    {json_ld}

    <style>
        :root {{
            --primary: {theme_tokens['primary']};
            --secondary: {theme_tokens['secondary']};
            --background: {bg_color};
            --surface: {theme_tokens['surface']};
            --text-color: {text_color};
        }}

        *, *::before, *::after {{
            box-sizing: border-box;
        }}

        body {{
            font-family: {font_family};
            margin: 0;
            padding: 0;
            background-color: var(--background);
            color: var(--text-color);
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
        }}

        a {{
            color: inherit;
        }}

        /* Touch target minimum standard: 48px x 48px (docs/DESIGN.md Section 3) */
        button, a.cta-btn {{
            min-height: 48px;
        }}

        /* Subtle responsive card elevation */
        .product-item-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 14px rgba(0, 0, 0, 0.08) !important;
        }}
    </style>
</head>
<body>
    <!-- Top Bounded Components Assembled per docs/DESIGN.md -->
    {hero_html}
    {products_html}
    {location_html}
    {contact_html}
    {footer_html}

    <!-- Persistent Floating Action Bar (docs/DESIGN.md Section 3) -->
    {fab_html}
</body>
</html>
"""
    return html_content
