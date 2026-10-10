"""Footer Component."""
from typing import Dict, Any, Optional


def render_footer(business_name: str, theme: Optional[Dict[str, Any]] = None) -> str:
    theme = theme or {}
    text_muted = "#9CA3AF"
    return f"""
    <footer id="footer" style="padding: 32px 20px 84px 20px; background: #111827; color: {text_muted}; text-align: center; font-size: 0.92rem; border-top: 1px solid #1F2937;">
        <div style="max-width: 820px; margin: 0 auto;">
            <p style="margin: 0 0 8px 0; color: #E5E7EB; font-weight: 600;">
                © 2026 {business_name}
            </p>
            <p style="margin: 0; font-size: 0.85rem; color: #9CA3AF;">
                Powered by <strong style="color: #FFFFFF;">KhojDoot</strong> • PS-29 Regional-Language No-Code Platform
            </p>
        </div>
    </footer>
    """
