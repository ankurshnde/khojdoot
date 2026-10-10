"""Hero Component.
Adheres to docs/DESIGN.md:
- Headline size: 2.25rem (mobile) / 3.0rem (desktop), weight 700
- Touch target >= 48px
- Theme colors from Palette Tokens
"""
from typing import Dict, Any, Optional


def render_hero(
    title: str,
    subtitle: str,
    phone: str,
    theme: Optional[Dict[str, Any]] = None,
    language: str = "mr-IN",
    theme_color: Optional[str] = None,
) -> str:
    theme = theme or {}
    primary = theme.get("primary") or theme_color or "#C84B31"
    secondary = theme.get("secondary", "#2D4059")
    text_color = "#FFFFFF"

    call_text = "📞 थेट कॉल करा / Call Now"
    if "te" in language:
        call_text = "📞 ఇప్పుడే కాల్ చేయండి / Call Now"
    elif "hi" in language:
        call_text = "📞 अभी कॉल करें / Call Now"
    elif "en" in language:
        call_text = "📞 Call Directly / Contact Us"

    phone_cta = ""
    if phone:
        phone_cta = f"""
        <div style="margin-top: 24px;">
            <a href="tel:{phone}" style="
                display: inline-flex;
                align-items: center;
                justify-content: center;
                min-height: 48px;
                min-width: 180px;
                background: #FFFFFF;
                color: {primary};
                padding: 12px 28px;
                font-size: 1.05rem;
                font-weight: 700;
                border-radius: 9999px;
                text-decoration: none;
                box-shadow: 0 4px 14px rgba(0, 0, 0, 0.18);
                transition: transform 0.15s ease;
            ">
                {call_text}
            </a>
        </div>
        """

    return f"""
    <section id="hero" class="hero-section" style="
        background: linear-gradient(135deg, {primary} 0%, {secondary} 100%);
        color: {text_color};
        padding: 56px 20px 48px 20px;
        text-align: center;
        position: relative;
    ">
        <div style="max-width: 820px; margin: 0 auto;">
            <span style="
                display: inline-block;
                background: rgba(255, 255, 255, 0.18);
                color: #FFFFFF;
                padding: 4px 14px;
                border-radius: 9999px;
                font-size: 0.85rem;
                font-weight: 600;
                letter-spacing: 0.05em;
                text-transform: uppercase;
                margin-bottom: 16px;
                border: 1px solid rgba(255, 255, 255, 0.3);
            ">
                ✓ Verified Indic Business
            </span>
            <h1 style="
                font-size: clamp(2.0rem, 5vw, 3.0rem);
                font-weight: 700;
                line-height: 1.25;
                margin: 0 0 16px 0;
                text-shadow: 0 2px 4px rgba(0, 0, 0, 0.15);
            ">
                {title}
            </h1>
            <p style="
                font-size: clamp(1.05rem, 2.5vw, 1.25rem);
                opacity: 0.95;
                max-width: 680px;
                margin: 0 auto;
                line-height: 1.55;
            ">
                {subtitle or 'विश्वसनीय स्थानिक व्यवसाय आणि तत्पर सेवा.'}
            </p>
            {phone_cta}
        </div>
    </section>
    """
