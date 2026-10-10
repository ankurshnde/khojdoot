"""Floating Action Bar (FAB) Component.
Mandated by docs/DESIGN.md Section 3:
- Minimum touch target >= 48px x 48px
- Call Now button (tel:+91...)
- WhatsApp button (https://wa.me/91...?text=...)
- Contrast ratio >= 4.5:1
"""
from typing import Dict, Any, Optional


def render_fab(
    phone: str,
    name: str,
    theme: Optional[Dict[str, Any]] = None,
    language: str = "mr-IN",
) -> str:
    if not phone:
        return ""

    theme = theme or {}
    primary = theme.get("primary", "#C84B31")
    clean_phone = "".join(filter(str.isdigit, phone))
    if len(clean_phone) == 10:
        clean_phone = "91" + clean_phone

    call_label = "📞 कॉल करा"
    wa_label = "💬 WhatsApp"
    if "te" in language:
        call_label = "📞 కాల్ చేయండి"
        wa_label = "💬 WhatsApp"
    elif "hi" in language:
        call_label = "📞 कॉल करें"
        wa_label = "💬 WhatsApp"
    elif "en" in language:
        call_label = "📞 Call Now"
        wa_label = "💬 WhatsApp"

    return f"""
    <!-- Mobile Floating Action Bar (Bharat Standard from docs/DESIGN.md) -->
    <div id="mobile-fab" style="
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        z-index: 9999;
        display: flex;
        gap: 12px;
        padding: 10px 16px;
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(8px);
        box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.12);
        border-top: 1px solid #E5E7EB;
        max-width: 600px;
        margin: 0 auto;
    ">
        <a href="tel:{phone}" style="
            flex: 1;
            min-height: 48px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: {primary};
            color: #FFFFFF;
            font-size: 15px;
            font-weight: 700;
            border-radius: 8px;
            text-decoration: none;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
            transition: transform 0.15s ease;
        ">
            {call_label}
        </a>
        <a href="https://wa.me/{clean_phone}?text=Hello%20{name}%2C%20I%20found%20your%20website%20on%20KhojDoot" target="_blank" style="
            flex: 1;
            min-height: 48px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #25D366;
            color: #FFFFFF;
            font-size: 15px;
            font-weight: 700;
            border-radius: 8px;
            text-decoration: none;
            box-shadow: 0 2px 8px rgba(37, 211, 102, 0.25);
            transition: transform 0.15s ease;
        ">
            {wa_label}
        </a>
    </div>
    """
