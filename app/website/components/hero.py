"""Hero Component."""
def render_hero(title: str, subtitle: str, phone: str, theme_color: str = "#E05A47") -> str:
    return f"""
    <section id="hero" class="hero" style="background: linear-gradient(135deg, {theme_color} 0%, #1a1a1a 100%); color: #fff; padding: 60px 20px; text-align: center;">
        <div style="max-width: 800px; margin: 0 auto;">
            <h1 style="font-size: 2.8rem; margin-bottom: 15px; font-weight: 700;">{title}</h1>
            <p style="font-size: 1.25rem; opacity: 0.9; margin-bottom: 30px;">{subtitle}</p>
            <a href="tel:{phone}" style="display: inline-block; background: #fff; color: {theme_color}; padding: 12px 30px; font-weight: bold; border-radius: 30px; text-decoration: none; box-shadow: 0 4px 10px rgba(0,0,0,0.15);">कॉल करा / Call Now</a>
        </div>
    </section>
    """
