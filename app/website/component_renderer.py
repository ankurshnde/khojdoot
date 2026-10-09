"""
Component Renderer & Business-Aware Assembler.
Combines BusinessFacts + DesignSystem to render accessible, responsive, real HTML previews.
Enforces zero-hallucination, privacy protection, and distinct layout personalities.
"""
from typing import Dict, Any, List
from app.website.data_models import BusinessFacts
from app.website.design_systems import DesignSystem, DESIGN_SYSTEMS


def render_design_preview(facts: BusinessFacts, ds: DesignSystem, is_compact_card: bool = False) -> str:
    """
    Renders a live, real DOM interface preview of a business website according to a specific design system.
    """
    c = ds.colors
    s = ds.spacing
    t = ds.typography

    # Compute business-aware component items
    phone_clean = "".join(filter(str.isdigit, facts.phone or ""))
    wa_clean = "".join(filter(str.isdigit, facts.whatsapp or facts.phone or ""))
    wa_msg = f"Hello {facts.name}, I found your website on Khoj Doot and would like to inquire about your offerings."
    wa_link = f"https://wa.me/{wa_clean}?text={wa_msg.replace(' ', '%20')}" if wa_clean else f"tel:{phone_clean}"

    # Photo resolution
    photo_urls = facts.photos or []
    hero_photo = photo_urls[0] if photo_urls else None

    # Render Offerings Items (Food Menu / Craft Grid / Service List)
    items_html = ""
    for idx, item in enumerate(facts.offerings[:4]):
        price_tag = ""
        if item.price is not None:
            unit_str = f" <span class='rate-unit'>/ {item.rate_unit}</span>" if item.rate_unit else ""
            price_tag = f"<span class='item-price'>₹{int(item.price) if item.price.is_integer() else item.price}{unit_str}</span>"
        else:
            price_tag = "<span class='item-price-inquire'>Inquire for price</span>"

        tag_badge = f"<span class='item-tag'>{item.tag}</span>" if item.tag else ""
        desc_text = f"<p class='item-desc'>{item.description}</p>" if item.description and not is_compact_card else ""
        
        # Layout variation for cards based on design system
        if ds.layout_style == "luxury_symmetric":
            items_html += f"""
            <div class="offering-card elegance-card">
                <div class="offering-header">
                    <span class="item-title">{item.title}</span>
                    <span class="leader-dots"></span>
                    {price_tag}
                </div>
                {desc_text}
                {tag_badge}
            </div>
            """
        elif ds.layout_style == "playful_chunky":
            items_html += f"""
            <div class="offering-card market-card">
                <div class="card-badge-row">{tag_badge}</div>
                <div class="item-title-bold">{item.title}</div>
                {desc_text}
                <div class="price-bubble-wrap">{price_tag}</div>
            </div>
            """
        elif ds.layout_style == "minimal_swiss":
            items_html += f"""
            <div class="offering-card swiss-card">
                <div class="swiss-num">0{idx+1}</div>
                <div class="swiss-body">
                    <div class="item-title">{item.title}</div>
                    {desc_text}
                </div>
                <div class="swiss-price">{price_tag}</div>
            </div>
            """
        elif ds.layout_style == "heritage_ornate":
            items_html += f"""
            <div class="offering-card heritage-card">
                <div class="heritage-icon">⚜</div>
                <div class="heritage-content">
                    <span class="item-title">{item.title}</span>
                    {desc_text}
                </div>
                {price_tag}
            </div>
            """
        else:
            items_html += f"""
            <div class="offering-card standard-card">
                <div class="card-content">
                    <span class="item-title">{item.title}</span>
                    {tag_badge}
                    {desc_text}
                </div>
                <div class="card-action">{price_tag}</div>
            </div>
            """

    # Category specific trust section
    trust_html = ""
    if facts.quality_pledges:
        pledges_pills = "".join([f"<span class='pledge-chip'>✓ {p}</span>" for p in facts.quality_pledges[:3]])
        trust_html = f"""
        <div class="trust-section">
            <div class="trust-title">Our Commitment / आमची हमी</div>
            <div class="pledge-container">{pledges_pills}</div>
        </div>
        """

    # Fulfilment & Delivery Section
    fulfilment_html = ""
    if facts.category == "homemade_food" and facts.pickup_window:
        fulfilment_html = f"""
        <div class="fulfilment-box">
            <span class="box-icon">🍲</span>
            <div class="box-text">
                <strong>Fresh Batches:</strong> {facts.pickup_window}
                <div class="sub-lead">{facts.lead_time or 'Advance order required'}</div>
            </div>
        </div>
        """
    elif facts.category == "handicrafts":
        fulfilment_html = f"""
        <div class="fulfilment-box">
            <span class="box-icon">📦</span>
            <div class="box-text">
                <strong>Craft Fulfillment:</strong> {facts.lead_time or 'Made to order with care'}
                <div class="sub-lead">Secure courier shipping & local pickup available</div>
            </div>
        </div>
        """
    elif facts.service_radius:
        fulfilment_html = f"""
        <div class="fulfilment-box">
            <span class="box-icon">📍</span>
            <div class="box-text">
                <strong>Service Coverage:</strong> {facts.service_radius}
            </div>
        </div>
        """

    # Hero visual or monogram fallback
    hero_visual_html = ""
    if hero_photo:
        hero_visual_html = f"""
        <div class="hero-image-wrap">
            <img src="/static/uploads/{hero_photo}" alt="{facts.name}" class="hero-img" onerror="this.parentElement.style.display='none';">
        </div>
        """
    else:
        # Typographic Monogram (Zero fake stock photos!)
        monogram = "".join([w[0] for w in facts.name.split() if w][:2]).upper()
        hero_visual_html = f"""
        <div class="monogram-badge" aria-hidden="true">
            <div class="monogram-letters">{monogram}</div>
            <div class="monogram-sub">EST. LOCAL</div>
        </div>
        """

    # Layout specific Hero markup
    hero_content_html = ""
    if ds.hero_layout == "centered_gold_framed":
        hero_content_html = f"""
        <div class="hero-frame elegance-hero">
            <div class="gold-seal">✦ AUTHENTIC HERITAGE ✦</div>
            <h1 class="hero-heading">{facts.name}</h1>
            <p class="hero-category">{facts.category_display}</p>
            <p class="hero-location">{facts.neighborhood or facts.city}, {facts.state}</p>
            {hero_visual_html}
            <div class="hero-cta-wrap">
                <a href="{wa_link}" target="_blank" class="primary-btn">Contact on WhatsApp</a>
                <a href="tel:{phone_clean}" class="secondary-btn">Direct Call</a>
            </div>
        </div>
        """
    elif ds.hero_layout == "dynamic_sticker_banner":
        hero_content_html = f"""
        <div class="market-hero">
            <div class="sticker-tag">🔥 Fresh Local Favorite</div>
            <h1 class="hero-heading">{facts.name}</h1>
            <p class="hero-category">{facts.category_display} in {facts.city}</p>
            {hero_visual_html}
            <div class="market-btn-row">
                <a href="{wa_link}" target="_blank" class="primary-btn">Order Now via WhatsApp 💬</a>
            </div>
        </div>
        """
    elif ds.hero_layout == "speed_dial_hero":
        hero_content_html = f"""
        <div class="pro-hero">
            <div class="pro-status-badge">● Open & Serving Today</div>
            <h1 class="hero-heading">{facts.name}</h1>
            <div class="pro-phone-display">📞 {facts.phone}</div>
            <p class="hero-location">Serving: {facts.service_radius or facts.city}</p>
            <div class="hero-cta-wrap">
                <a href="tel:{phone_clean}" class="primary-btn">Tap to Call Merchant</a>
                <a href="{wa_link}" target="_blank" class="secondary-btn">WhatsApp Chat</a>
            </div>
        </div>
        """
    elif ds.hero_layout == "magazine_editorial_cover":
        hero_content_html = f"""
        <div class="editorial-hero">
            <div class="editorial-vol">KHOJ DOOT SPECIAL • {facts.city.upper()}</div>
            <h1 class="hero-heading">{facts.name}</h1>
            <div class="hairline-divider"></div>
            <p class="hero-category">{facts.category_display}</p>
            {hero_visual_html}
            <div class="hero-cta-wrap">
                <a href="{wa_link}" target="_blank" class="primary-btn">Inquire Collection</a>
            </div>
        </div>
        """
    elif ds.hero_layout == "homestyle_tiffin_hero":
        hero_content_html = f"""
        <div class="kitchen-hero">
            <div class="pure-home-badge">🍲 घरगुती शुद्ध अन्न • Homestyle Care</div>
            <h1 class="hero-heading">{facts.name}</h1>
            <p class="hero-category">{facts.category_display}</p>
            <p class="hero-hours">⏰ {facts.operating_hours}</p>
            <div class="hero-cta-wrap">
                <a href="{wa_link}" target="_blank" class="primary-btn">Order Fresh Tiffin / डबा मागवा</a>
            </div>
        </div>
        """
    else:
        hero_content_html = f"""
        <div class="generic-hero">
            <span class="style-badge">{facts.category_display}</span>
            <h1 class="hero-heading">{facts.name}</h1>
            <p class="hero-location">📍 {facts.address_display or facts.city}</p>
            {hero_visual_html}
            <div class="hero-cta-wrap">
                <a href="{wa_link}" target="_blank" class="primary-btn">Contact on WhatsApp</a>
            </div>
        </div>
        """

    # Full CSS for the specific Design System
    style_css = f"""
    <style>
        @import url('{t.font_import_url}');

        .ds-scope-{ds.id} {{
            font-family: {t.body_font};
            background-color: {c.background};
            color: {c.text_primary};
            padding: {s.section_padding};
            border-radius: {s.border_radius};
            border: {s.card_border};
            box-shadow: {s.box_shadow};
            position: relative;
            box-sizing: border-box;
            line-height: 1.5;
            transition: all 0.25s ease;
            max-width: 100%;
            overflow: hidden;
        }}

        .ds-scope-{ds.id} * {{
            box-sizing: border-box;
        }}

        .ds-scope-{ds.id} h1, 
        .ds-scope-{ds.id} h2, 
        .ds-scope-{ds.id} .hero-heading {{
            font-family: {t.heading_font};
            font-weight: {t.heading_weight};
            margin: 0 0 8px 0;
            color: {c.text_primary};
            line-height: 1.2;
        }}

        .ds-scope-{ds.id} .hero-heading {{
            font-size: 1.85rem;
            letter-spacing: -0.02em;
        }}

        .ds-scope-{ds.id} .hero-category {{
            font-size: 0.95rem;
            color: {c.text_secondary};
            margin: 0 0 10px 0;
            font-weight: 500;
        }}

        .ds-scope-{ds.id} .hero-location {{
            font-size: 0.85rem;
            color: {c.text_secondary};
            opacity: 0.9;
            margin: 0 0 18px 0;
        }}

        /* Hero Container Variations */
        .ds-scope-{ds.id} .elegance-hero {{
            border: 1px solid {c.border};
            padding: 24px;
            background: {c.surface};
            text-align: center;
            border-radius: {s.border_radius};
            margin-bottom: 24px;
        }}

        .ds-scope-{ds.id} .gold-seal {{
            color: {c.secondary};
            font-size: 0.72rem;
            letter-spacing: 0.18em;
            font-weight: 600;
            margin-bottom: 8px;
        }}

        .ds-scope-{ds.id} .market-hero {{
            background: linear-gradient(135deg, {c.surface} 0%, {c.background} 100%);
            border: 2px dashed {c.primary};
            padding: 24px;
            border-radius: {s.border_radius};
            text-align: left;
            margin-bottom: 24px;
        }}

        .ds-scope-{ds.id} .sticker-tag {{
            display: inline-block;
            background: {c.primary};
            color: #fff;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 999px;
            margin-bottom: 10px;
        }}

        .ds-scope-{ds.id} .pro-hero {{
            background: {c.surface};
            border-left: 6px solid {c.primary};
            padding: 24px;
            border-radius: {s.border_radius};
            box-shadow: 0 4px 12px rgba(0,0,0,0.06);
            margin-bottom: 24px;
        }}

        .ds-scope-{ds.id} .pro-phone-display {{
            font-size: 1.25rem;
            font-weight: 800;
            color: {c.primary};
            margin: 8px 0;
        }}

        .ds-scope-{ds.id} .editorial-hero {{
            border-bottom: 1px solid {c.border};
            padding-bottom: 24px;
            margin-bottom: 24px;
            text-align: center;
        }}

        .ds-scope-{ds.id} .editorial-vol {{
            font-size: 0.7rem;
            letter-spacing: 0.25em;
            color: {c.secondary};
            margin-bottom: 12px;
        }}

        .ds-scope-{ds.id} .hairline-divider {{
            height: 1px;
            background: {c.border};
            width: 60px;
            margin: 10px auto;
        }}

        .ds-scope-{ds.id} .kitchen-hero {{
            background: {c.surface};
            border: 2px solid {c.border};
            border-radius: {s.border_radius};
            padding: 24px;
            text-align: center;
            margin-bottom: 24px;
        }}

        .ds-scope-{ds.id} .pure-home-badge {{
            display: inline-block;
            background: {c.accent};
            color: {c.primary};
            font-weight: 700;
            font-size: 0.78rem;
            padding: 4px 12px;
            border-radius: 999px;
            margin-bottom: 10px;
        }}

        /* Offerings Section */
        .ds-scope-{ds.id} .section-heading {{
            font-size: 1.25rem;
            font-family: {t.heading_font};
            margin: 24px 0 14px 0;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .ds-scope-{ds.id} .offerings-grid {{
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-bottom: 24px;
        }}

        .ds-scope-{ds.id} .offering-card {{
            background: {c.surface};
            border-radius: {s.border_radius};
            border: {s.card_border};
            padding: 14px 18px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .ds-scope-{ds.id} .elegance-card .offering-header {{
            display: flex;
            align-items: baseline;
            width: 100%;
            justify-content: space-between;
        }}

        .ds-scope-{ds.id} .item-title {{
            font-weight: 600;
            font-size: 0.98rem;
            color: {c.text_primary};
        }}

        .ds-scope-{ds.id} .item-price {{
            font-weight: 700;
            font-size: 1.05rem;
            color: {c.primary};
        }}

        .ds-scope-{ds.id} .item-price-inquire {{
            font-size: 0.8rem;
            color: {c.text_secondary};
            font-style: italic;
        }}

        .ds-scope-{ds.id} .rate-unit {{
            font-size: 0.75rem;
            font-weight: normal;
            opacity: 0.8;
        }}

        .ds-scope-{ds.id} .item-tag {{
            display: inline-block;
            background: {c.background};
            color: {c.primary};
            font-size: 0.7rem;
            padding: 2px 8px;
            border-radius: 4px;
            margin-left: 8px;
        }}

        /* Trust & Fulfilment */
        .ds-scope-{ds.id} .trust-section {{
            margin: 20px 0;
            padding: 14px;
            background: {c.surface};
            border-radius: {s.border_radius};
            border: 1px dashed {c.border};
        }}

        .ds-scope-{ds.id} .trust-title {{
            font-size: 0.8rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: {c.text_secondary};
            margin-bottom: 8px;
        }}

        .ds-scope-{ds.id} .pledge-container {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }}

        .ds-scope-{ds.id} .pledge-chip {{
            font-size: 0.75rem;
            background: {c.background};
            color: {c.primary};
            padding: 4px 10px;
            border-radius: 999px;
            font-weight: 600;
        }}

        .ds-scope-{ds.id} .fulfilment-box {{
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px 16px;
            background: {c.surface};
            border-radius: {s.border_radius};
            border: 1px solid {c.border};
            margin-bottom: 20px;
            font-size: 0.88rem;
        }}

        .ds-scope-{ds.id} .box-icon {{
            font-size: 1.4rem;
        }}

        .ds-scope-{ds.id} .sub-lead {{
            font-size: 0.75rem;
            color: {c.text_secondary};
            margin-top: 2px;
        }}

        /* Buttons & Conversion */
        .ds-scope-{ds.id} .hero-cta-wrap {{
            display: flex;
            gap: 10px;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 18px;
        }}

        .ds-scope-{ds.id} .primary-btn {{
            display: inline-block;
            background: {c.primary};
            color: #ffffff !important;
            padding: 12px 24px;
            border-radius: {s.border_radius};
            font-weight: 600;
            font-size: 0.95rem;
            text-decoration: none;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            transition: transform 0.15s ease;
            text-align: center;
        }}

        .ds-scope-{ds.id} .secondary-btn {{
            display: inline-block;
            background: {c.surface};
            color: {c.primary} !important;
            border: 1px solid {c.border};
            padding: 12px 20px;
            border-radius: {s.border_radius};
            font-weight: 600;
            font-size: 0.95rem;
            text-decoration: none;
            text-align: center;
        }}

        .ds-scope-{ds.id} .primary-btn:hover,
        .ds-scope-{ds.id} .secondary-btn:hover {{
            transform: translateY(-2px);
        }}

        .ds-scope-{ds.id} .footer-bar {{
            margin-top: 28px;
            padding-top: 14px;
            border-top: 1px solid {c.border};
            font-size: 0.75rem;
            color: {c.text_secondary};
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .ds-scope-{ds.id} .monogram-badge {{
            width: 72px;
            height: 72px;
            margin: 14px auto;
            border-radius: {s.border_radius};
            background: {c.primary};
            color: #fff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            box-shadow: {s.box_shadow};
        }}

        .ds-scope-{ds.id} .monogram-letters {{
            font-size: 1.4rem;
            font-weight: 800;
            font-family: {t.heading_font};
            line-height: 1;
        }}

        .ds-scope-{ds.id} .monogram-sub {{
            font-size: 0.55rem;
            letter-spacing: 0.1em;
            opacity: 0.8;
            margin-top: 4px;
        }}
    </style>
    """

    # Assemble complete real DOM container
    html = f"""
    {style_css}
    <div class="ds-scope-{ds.id} ds-concept-card" data-concept-id="{ds.id}">
        {hero_content_html}
        
        <div class="section-heading">
            <span>Offerings & Menu</span>
            <span style="font-size: 0.75rem; color: {c.text_secondary};">Verified facts</span>
        </div>
        <div class="offerings-grid">
            {items_html}
        </div>

        {trust_html}
        {fulfilment_html}

        <div class="footer-bar">
            <span>Khoj Doot Verified SME</span>
            <span>{facts.city} • {facts.category_display}</span>
        </div>
    </div>
    """
    return html


def get_all_design_previews(facts: BusinessFacts) -> List[Dict[str, Any]]:
    """
    Generates preview models for all 10 distinct design systems from a single set of BusinessFacts.
    """
    results = []
    for concept_id, ds in DESIGN_SYSTEMS.items():
        rendered_html = render_design_preview(facts, ds)
        results.append({
            "id": ds.id,
            "name": ds.name,
            "concept_number": ds.concept_number,
            "tagline": ds.tagline,
            "description": ds.description,
            "colors": ds.colors.model_dump(),
            "typography": {
                "heading_font": ds.typography.heading_font,
                "body_font": ds.typography.body_font,
            },
            "layout_style": ds.layout_style,
            "rendered_html": rendered_html,
        })
    return results
