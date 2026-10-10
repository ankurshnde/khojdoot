"""Contact & WhatsApp Action Component.
Adheres to docs/DESIGN.md:
- Minimum touch target >= 48px x 48px
- Direct Call Now button (tel:+91...)
- Direct WhatsApp Order button (https://wa.me/...)
"""
from typing import Dict, Any, Optional


def render_contact(
    phone: str,
    name: str,
    theme: Optional[Dict[str, Any]] = None,
    language: str = "mr-IN",
) -> str:
    if not phone:
        return ""

    theme = theme or {}
    primary = theme.get("primary", "#C84B31")
    text_color = theme.get("text", "#1F2937")

    clean_phone = "".join(filter(str.isdigit, phone))
    if len(clean_phone) == 10:
        clean_phone = "91" + clean_phone

    section_title = "संपर्क साधा आणि ऑर्डर करा / Get In Touch"
    call_label = f"📞 थेट कॉल: {phone}"
    wa_label = "💬 WhatsApp वर ऑर्डर करा"
    if "te" in language:
        section_title = "సంప్రదించండి & ఆర్డర్ చేయండి / Contact & Order"
        call_label = f"📞 కాల్ చేయండి: {phone}"
        wa_label = "💬 WhatsApp చాట్ & ఆర్డర్"
    elif "hi" in language:
        section_title = "सीधे संपर्क करें या ऑर्डर दें / Contact Us"
        call_label = f"📞 सीधे कॉल करें: {phone}"
        wa_label = "💬 WhatsApp पर ऑर्डर भेजें"
    elif "en" in language:
        section_title = "Get In Touch & Order Online"
        call_label = f"📞 Direct Call: {phone}"
        wa_label = "💬 Chat & Order on WhatsApp"

    return f"""
    <section id="contact" class="contact-section" style="padding: 48px 20px 72px 20px; text-align: center; max-width: 820px; margin: 0 auto;">
        <h2 style="font-size: clamp(1.5rem, 3.8vw, 1.95rem); margin-bottom: 20px; color: {text_color}; font-weight: 700;">
            {section_title}
        </h2>
        <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap;">
            <a href="tel:{phone}" style="
                min-height: 48px;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                background: {primary};
                color: #FFFFFF;
                padding: 12px 28px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: 700;
                font-size: 1.05rem;
                box-shadow: 0 4px 12px rgba(0,0,0,0.12);
                transition: transform 0.15s ease;
            ">
                {call_label}
            </a>
            <a href="https://wa.me/{clean_phone}?text=Hello%20{name}%2C%20I%20want%20to%20order%20from%20your%20website" target="_blank" style="
                min-height: 48px;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                background: #25D366;
                color: #FFFFFF;
                padding: 12px 28px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: 700;
                font-size: 1.05rem;
                box-shadow: 0 4px 12px rgba(37, 211, 102, 0.25);
                transition: transform 0.15s ease;
            ">
                {wa_label}
            </a>
        </div>
    </section>
    """
