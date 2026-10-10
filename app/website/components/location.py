"""Location and Working Hours Component.
Adheres to docs/DESIGN.md:
- Structured shop address & timings
- Accessible contrast & typography
"""
from typing import Dict, Any, Optional


def render_location(
    location: str,
    hours: str,
    theme: Optional[Dict[str, Any]] = None,
    language: str = "mr-IN",
) -> str:
    theme = theme or {}
    surface = theme.get("surface", "#FFFFFF")
    text_color = theme.get("text", "#1F2937")

    section_title = "पत्ता आणि वेळ / Location & Hours"
    addr_label = "📍 दुकानाचा पत्ता:"
    hours_label = "⏰ सेवेची वेळ:"
    if "te" in language:
        section_title = "చిరునామా & పని వేళలు / Location & Timings"
        addr_label = "📍 చిరునామా:"
        hours_label = "⏰ సమయం:"
    elif "hi" in language:
        section_title = "दुकान का पता एवं समय / Location & Hours"
        addr_label = "📍 पूरा पता:"
        hours_label = "⏰ खुलने का समय:"
    elif "en" in language:
        section_title = "Location & Operating Timings"
        addr_label = "📍 Address / Area:"
        hours_label = "⏰ Operating Hours:"

    loc_val = location or "स्थानिक बाजारपेठ (Local Area)"
    hrs_val = hours or "सकाळी ९:०० ते रात्री ९:०० (9:00 AM - 9:00 PM)"

    return f"""
    <section id="location" class="location-section" style="padding: 40px 20px; background: rgba(0, 0, 0, 0.02); text-align: center;">
        <div style="max-width: 820px; margin: 0 auto;">
            <h2 style="font-size: clamp(1.4rem, 3.5vw, 1.85rem); margin-bottom: 24px; color: {text_color}; font-weight: 700;">
                {section_title}
            </h2>
            <div style="
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
                gap: 16px;
                text-align: left;
            ">
                <div style="
                    background: {surface};
                    padding: 20px 22px;
                    border-radius: 10px;
                    border: 1px solid #E5E7EB;
                    box-shadow: 0 2px 6px rgba(0,0,0,0.03);
                ">
                    <strong style="font-size: 1.05rem; color: #111; display: block; margin-bottom: 6px;">{addr_label}</strong>
                    <span style="font-size: 1.0rem; color: #4B5563; line-height: 1.45;">{loc_val}</span>
                </div>
                <div style="
                    background: {surface};
                    padding: 20px 22px;
                    border-radius: 10px;
                    border: 1px solid #E5E7EB;
                    box-shadow: 0 2px 6px rgba(0,0,0,0.03);
                ">
                    <strong style="font-size: 1.05rem; color: #111; display: block; margin-bottom: 6px;">{hours_label}</strong>
                    <span style="font-size: 1.0rem; color: #4B5563; line-height: 1.45;">{hrs_val}</span>
                </div>
            </div>
        </div>
    </section>
    """
