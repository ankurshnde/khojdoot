"""Footer Component."""
def render_footer(business_name: str) -> str:
    return f"""
    <footer id="footer" style="padding: 30px 20px; background: #111; color: #aaa; text-align: center; font-size: 0.9rem;">
        <p>© 2026 {business_name}. Powered by <strong style="color: #fff;">KhojDoot</strong> (PS-29 Regional No-Code).</p>
    </footer>
    """
