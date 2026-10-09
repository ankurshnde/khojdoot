"""Location and Working Hours Component."""
def render_location(location: str, hours: str) -> str:
    return f"""
    <section id="location" class="location" style="padding: 40px 20px; background: #f9f9f9; text-align: center;">
        <div style="max-width: 800px; margin: 0 auto;">
            <h2 style="font-size: 1.8rem; margin-bottom: 20px;">पत्ता आणि वेळ / Location & Hours</h2>
            <p style="font-size: 1.1rem; margin-bottom: 10px;">📍 <strong>पत्ता:</strong> {location}</p>
            <p style="font-size: 1.1rem; color: #555;">⏰ <strong>वेळ:</strong> {hours}</p>
        </div>
    </section>
    """
