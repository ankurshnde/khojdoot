"""
Ten Distinct Design System Definitions & Visual Tokens.
Controls colors, typography, spacing, border-radius, shadows, and layout behavior.
"""
from typing import Dict, Any, List
from pydantic import BaseModel


class ColorPalette(BaseModel):
    primary: str
    secondary: str
    background: str
    surface: str
    text_primary: str
    text_secondary: str
    accent: str
    border: str


class TypographySpec(BaseModel):
    heading_font: str
    body_font: str
    heading_weight: str = "700"
    body_weight: str = "400"
    font_import_url: str


class SpacingAndBorder(BaseModel):
    border_radius: str
    card_border: str
    box_shadow: str
    section_padding: str
    element_gap: str


class DesignSystem(BaseModel):
    id: str
    name: str
    concept_number: int
    tagline: str
    description: str
    colors: ColorPalette
    typography: TypographySpec
    layout_style: str  # luxury_symmetric, playful_chunky, organic_earthy, modern_grid, heritage_ornate, utility_bold, editorial_fashion, kitchen_cozy, minimal_swiss, global_tapestry
    spacing: SpacingAndBorder
    hero_layout: str
    card_layout: str
    cta_style: str
    badge_style: str


# ==============================================================================
# 10 STRUCTURED DESIGN SYSTEMS
# ==============================================================================

DESIGN_SYSTEMS: Dict[str, DesignSystem] = {
    # 1. Timeless Elegance (First fully polished concept)
    "timeless_elegance": DesignSystem(
        id="timeless_elegance",
        name="Timeless Elegance",
        concept_number=1,
        tagline="Refined luxury, classic symmetry, and antique gold elegance.",
        description="A prestigious, heritage-inspired design system with deep forest green, warm ivory backdrop, and delicate antique gold accents. Ideal for premium homemade delicacies and high-value crafts.",
        colors=ColorPalette(
            primary="#19372C",      # Forest green
            secondary="#D9C49A",    # Antique gold
            background="#F5F0E5",   # Warm ivory
            surface="#FFFFFF",      # Pure card background
            text_primary="#19372C", # Forest green dark text
            text_secondary="#684A3D",# Espresso brown
            accent="#526157",       # Slate olive
            border="#D9C49A",       # Antique gold border
        ),
        typography=TypographySpec(
            heading_font="'Playfair Display', serif, Georgia",
            body_font="'Inter', sans-serif, system-ui",
            heading_weight="700",
            body_weight="400",
            font_import_url="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap",
        ),
        layout_style="luxury_symmetric",
        spacing=SpacingAndBorder(
            border_radius="6px",
            card_border="1px solid #D9C49A",
            box_shadow="0 8px 24px rgba(25, 55, 44, 0.08)",
            section_padding="48px 24px",
            element_gap="20px",
        ),
        hero_layout="centered_gold_framed",
        card_layout="gold_leaf_leader_card",
        cta_style="forest_gold_button",
        badge_style="antique_gold_pill",
    ),

    # 2. Playful Market
    "playful_market": DesignSystem(
        id="playful_market",
        name="Playful Market",
        concept_number=2,
        tagline="Bustling neighborhood market warmth, vibrant badges, and joyful rounded shapes.",
        description="Energetic, approachable design featuring mango orange and sunshine yellow with chunky rounded borders. Perfect for bustling snack makers, festive lanterns, and community sellers.",
        colors=ColorPalette(
            primary="#FF6B35",      # Mango orange
            secondary="#F7C548",    # Sunshine yellow
            background="#FFFDF9",   # Fresh cream
            surface="#FFFFFF",      # Crisp white
            text_primary="#2B2D42", # Deep charcoal
            text_secondary="#D85A38",# Terracotta
            accent="#2E86AB",       # Sky blue
            border="#FFE5D9",       # Soft peach border
        ),
        typography=TypographySpec(
            heading_font="'Poppins', 'Fredoka', sans-serif",
            body_font="'Quicksand', sans-serif",
            heading_weight="700",
            body_weight="500",
            font_import_url="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Quicksand:wght@500;600;700&display=swap",
        ),
        layout_style="playful_chunky",
        spacing=SpacingAndBorder(
            border_radius="20px",
            card_border="2px solid #FFE5D9",
            box_shadow="0 10px 25px rgba(255, 107, 53, 0.12)",
            section_padding="40px 20px",
            element_gap="16px",
        ),
        hero_layout="dynamic_sticker_banner",
        card_layout="chunky_bouncy_cards",
        cta_style="mango_bubble_button",
        badge_style="sticker_pill",
    ),

    # 3. Natural Craft
    "natural_craft": DesignSystem(
        id="natural_craft",
        name="Natural Craft",
        concept_number=3,
        tagline="Earthy organic textures, botanical hues, and maker-first sincerity.",
        description="Grounded in moss green, clay terracotta, and raw oatmeal linen. Celebrates authentic raw materials, eco-friendly candles, terracotta decor, and hand-ground spices.",
        colors=ColorPalette(
            primary="#3E5638",      # Moss green
            secondary="#A2674B",    # Clay terracotta
            background="#F7F4EE",   # Warm oatmeal
            surface="#FFFFFF",      # Off-white card
            text_primary="#2B2D26", # Bark charcoal
            text_secondary="#6B705C",# Olive earth
            accent="#E8DFD0",       # Sand beige
            border="#D3C7B6",       # Linen border
        ),
        typography=TypographySpec(
            heading_font="'Lora', serif",
            body_font="'Plus Jakarta Sans', sans-serif",
            heading_weight="600",
            body_weight="400",
            font_import_url="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;1,500&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap",
        ),
        layout_style="organic_earthy",
        spacing=SpacingAndBorder(
            border_radius="10px",
            card_border="1.5px solid #D3C7B6",
            box_shadow="0 4px 16px rgba(43, 45, 38, 0.06)",
            section_padding="44px 22px",
            element_gap="18px",
        ),
        hero_layout="botanical_split_narrative",
        card_layout="natural_linen_card",
        cta_style="moss_clay_button",
        badge_style="earth_leaf_pill",
    ),

    # 4. Modern Studio
    "modern_studio": DesignSystem(
        id="modern_studio",
        name="Modern Studio",
        concept_number=4,
        tagline="Architectural clean lines, electric cobalt accents, and crisp typography.",
        description="Contemporary aesthetic with deep indigo, electric cobalt, and pure white cards. Appeals to modern computer embroidery studios, high-precision designers, and urban artisans.",
        colors=ColorPalette(
            primary="#1A1E2E",      # Deep indigo
            secondary="#2A52BE",    # Electric cobalt
            background="#F8FAFC",   # Clean snow
            surface="#FFFFFF",      # Pure white
            text_primary="#0F172A", # Dark slate graphite
            text_secondary="#64748B",# Cool slate
            accent="#94A3B8",       # Ash silver
            border="#E2E8F0",       # Crisp divider border
        ),
        typography=TypographySpec(
            heading_font="'Space Grotesk', sans-serif",
            body_font="'DM Sans', sans-serif",
            heading_weight="700",
            body_weight="400",
            font_import_url="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Space+Grotesk:wght@600;700&display=swap",
        ),
        layout_style="modern_grid",
        spacing=SpacingAndBorder(
            border_radius="4px",
            card_border="1px solid #E2E8F0",
            box_shadow="0 2px 8px rgba(15, 23, 42, 0.05)",
            section_padding="48px 24px",
            element_gap="20px",
        ),
        hero_layout="architectural_split_grid",
        card_layout="clean_grid_specs_card",
        cta_style="cobalt_sharp_button",
        badge_style="mono_tag_badge",
    ),

    # 5. Local Heritage
    "local_heritage": DesignSystem(
        id="local_heritage",
        name="Local Heritage",
        concept_number=5,
        tagline="Cultural Marathi warmth, kesari saffron, and traditional brass motifs.",
        description="Infused with deep royal indigo, festive saffron (केशरी), and haldi gold on vintage parchment. Ideal for traditional Maharashtrian tiffin services, festival lanterns, and silk creations.",
        colors=ColorPalette(
            primary="#1B2A4A",      # Royal indigo
            secondary="#E05A1B",    # Kesari saffron
            background="#FBF6ED",   # Vintage parchment
            surface="#FFFFFF",      # Warm card
            text_primary="#1B2A4A", # Indigo title
            text_secondary="#5C1D24",# Deep maroon
            accent="#E5A93C",       # Haldi gold
            border="#EAD8BE",       # Brass parchment border
        ),
        typography=TypographySpec(
            heading_font="'Rozha One', 'Noto Serif Devanagari', serif",
            body_font="'Mukta', sans-serif",
            heading_weight="700",
            body_weight="500",
            font_import_url="https://fonts.googleapis.com/css2?family=Mukta:wght@400;500;700&family=Rozha+One&display=swap",
        ),
        layout_style="heritage_ornate",
        spacing=SpacingAndBorder(
            border_radius="12px",
            card_border="2px solid #EAD8BE",
            box_shadow="0 6px 20px rgba(92, 29, 36, 0.08)",
            section_padding="42px 20px",
            element_gap="18px",
        ),
        hero_layout="ornate_arch_banner",
        card_layout="heritage_thali_card",
        cta_style="kesari_brass_button",
        badge_style="marigold_seal_pill",
    ),

    # 6. Neighborhood Pro
    "neighborhood_pro": DesignSystem(
        id="neighborhood_pro",
        name="Neighborhood Pro",
        concept_number=6,
        tagline="High-trust utility, instant phone access, and no-nonsense reliability.",
        description="Built for immediate phone calls and local service verification. Solid trust navy and alert amber, emphasizing operating hours, exact neighborhood location, and clear turnaround times.",
        colors=ColorPalette(
            primary="#0F3460",      # Trust navy
            secondary="#E94560",    # Urgent amber red
            background="#F0F4F8",   # Cool utility slate
            surface="#FFFFFF",      # Crisp white
            text_primary="#0F3460", # Navy text
            text_secondary="#475569",# Slate steel
            accent="#533483",       # Steel purple
            border="#CBD5E1",       # Utility border
        ),
        typography=TypographySpec(
            heading_font="'Archivo', sans-serif",
            body_font="'Roboto', sans-serif",
            heading_weight="800",
            body_weight="400",
            font_import_url="https://fonts.googleapis.com/css2?family=Archivo:wght@700;800;900&family=Roboto:wght@400;500;700&display=swap",
        ),
        layout_style="utility_bold",
        spacing=SpacingAndBorder(
            border_radius="8px",
            card_border="2px solid #CBD5E1",
            box_shadow="0 4px 12px rgba(15, 52, 96, 0.08)",
            section_padding="36px 18px",
            element_gap="16px",
        ),
        hero_layout="speed_dial_hero",
        card_layout="utility_rate_card",
        cta_style="direct_call_now_button",
        badge_style="emergency_status_pill",
    ),

    # 7. Boutique Editorial
    "boutique_editorial": DesignSystem(
        id="boutique_editorial",
        name="Boutique Editorial",
        concept_number=7,
        tagline="Haute-couture magazine aesthetic, delicate hairlines, and generous whitespace.",
        description="Fashion magazine layout with noir black, champagne silk, and blush marble. Focuses on artisanal jewellery, tailored blouse designs, and luxury handcrafted accessories.",
        colors=ColorPalette(
            primary="#111111",      # Noir black
            secondary="#9E8B7D",    # Cashmere taupe
            background="#FAF7F5",   # Blush marble
            surface="#FFFFFF",      # Silk white
            text_primary="#111111", # Pure black
            text_secondary="#736B66",# Muted cashmere
            accent="#EFE9E0",       # Champagne silk
            border="#E5DDD5",       # Hairline border
        ),
        typography=TypographySpec(
            heading_font="'Cormorant Garamond', serif",
            body_font="'Work Sans', sans-serif",
            heading_weight="600",
            body_weight="300",
            font_import_url="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Work+Sans:wght@300;400;500&display=swap",
        ),
        layout_style="editorial_fashion",
        spacing=SpacingAndBorder(
            border_radius="0px",
            card_border="1px solid #E5DDD5",
            box_shadow="none",
            section_padding="56px 28px",
            element_gap="24px",
        ),
        hero_layout="magazine_editorial_cover",
        card_layout="asymmetric_fashion_card",
        cta_style="minimal_noir_button",
        badge_style="couture_italic_tag",
    ),

    # 8. Home Kitchen
    "home_kitchen": DesignSystem(
        id="home_kitchen",
        name="Home Kitchen",
        concept_number=8,
        tagline="Cozy dining-table warmth, fresh meal badges, and mother's kitchen sincerity.",
        description="Appetizing terracotta clay, sage herb green, and butter cream. Highlights portion-based pricing, daily lunch/dinner batch cutoff times, and authentic home-cooked hygiene.",
        colors=ColorPalette(
            primary="#C85A32",      # Terracotta clay
            secondary="#6E8B74",    # Sage leaf green
            background="#FCFAF6",   # Warm steam white
            surface="#FFFFFF",      # Recipe card white
            text_primary="#4A2E2B", # Cinnamon brown
            text_secondary="#7A584E",# Roasted coffee
            accent="#FFF6E5",       # Fresh butter
            border="#F0E3D3",       # Warm butter border
        ),
        typography=TypographySpec(
            heading_font="'Merriweather', serif",
            body_font="'Open Sans', sans-serif",
            heading_weight="700",
            body_weight="400",
            font_import_url="https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,700;1,400&family=Open+Sans:wght@400;600;700&display=swap",
        ),
        layout_style="kitchen_cozy",
        spacing=SpacingAndBorder(
            border_radius="16px",
            card_border="1.5px solid #F0E3D3",
            box_shadow="0 6px 18px rgba(200, 90, 50, 0.07)",
            section_padding="40px 20px",
            element_gap="18px",
        ),
        hero_layout="homestyle_tiffin_hero",
        card_layout="recipe_portion_card",
        cta_style="clay_tiffin_order_button",
        badge_style="pure_veg_home_pill",
    ),

    # 9. Minimal Atelier
    "minimal_atelier": DesignSystem(
        id="minimal_atelier",
        name="Minimal Atelier",
        concept_number=9,
        tagline="Monochrome restraint, Swiss precision, and zero-distraction focus on the work.",
        description="Ultra-clean Swiss grid with deep onyx, pale fog background, and razor-thin borders. Great for modern artisans, custom candle makers, and high-end niche makers.",
        colors=ColorPalette(
            primary="#121212",      # Deep onyx
            secondary="#6E6E73",    # Slate gray
            background="#F4F4F6",   # Pale fog
            surface="#FFFFFF",      # Crisp titanium white
            text_primary="#121212", # Pitch black
            text_secondary="#6E6E73",# Neutral gray
            accent="#000000",       # Jet black
            border="#E2E2E8",       # Concrete hairline
        ),
        typography=TypographySpec(
            heading_font="'Syne', sans-serif",
            body_font="'Inter', sans-serif",
            heading_weight="700",
            body_weight="400",
            font_import_url="https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=Syne:wght@600;700;800&display=swap",
        ),
        layout_style="minimal_swiss",
        spacing=SpacingAndBorder(
            border_radius="2px",
            card_border="1px solid #E2E2E8",
            box_shadow="0 1px 3px rgba(0, 0, 0, 0.04)",
            section_padding="50px 24px",
            element_gap="22px",
        ),
        hero_layout="monochrome_atelier_hero",
        card_layout="swiss_numbered_item_card",
        cta_style="onyx_minimal_button",
        badge_style="stark_mono_pill",
    ),

    # 10. Global Artisan
    "global_artisan": DesignSystem(
        id="global_artisan",
        name="Global Artisan",
        concept_number=10,
        tagline="Export packaging pedigree, provenance stamps, and cross-border storytelling.",
        description="Rich lapis lazuli, terracotta spice, and cardamom green on raw linen. Highlights regional origin pride, export-safe courier packaging, and handmade international appeal.",
        colors=ColorPalette(
            primary="#183059",      # Lapis lazuli
            secondary="#B65134",    # Terracotta spice
            background="#F5F2EB",   # Raw woven linen
            surface="#FFFFFF",      # Pure card
            text_primary="#183059", # Lapis text
            text_secondary="#405944",# Cardamom green
            accent="#E8985E",       # Raw amber
            border="#DCCFB8",       # Tapestry border
        ),
        typography=TypographySpec(
            heading_font="'Marcellus', serif",
            body_font="'Outfit', sans-serif",
            heading_weight="400",
            body_weight="400",
            font_import_url="https://fonts.googleapis.com/css2?family=Marcellus&family=Outfit:wght@400;500;600&display=swap",
        ),
        layout_style="global_tapestry",
        spacing=SpacingAndBorder(
            border_radius="14px",
            card_border="2px solid #DCCFB8",
            box_shadow="0 8px 24px rgba(24, 48, 89, 0.09)",
            section_padding="46px 22px",
            element_gap="20px",
        ),
        hero_layout="provenance_tapestry_hero",
        card_layout="export_provenance_card",
        cta_style="lapis_artisan_button",
        badge_style="origin_stamp_pill",
    ),
}
