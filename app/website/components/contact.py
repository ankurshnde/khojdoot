"""Contact & WhatsApp Action Component."""
def render_contact(phone: str, name: str) -> str:
    clean_phone = phone.replace(" ", "").replace("+", "")
    return f"""
    <section id="contact" class="contact" style="padding: 40px 20px; text-align: center;">
        <div style="max-width: 800px; margin: 0 auto;">
            <h2 style="font-size: 1.8rem; margin-bottom: 20px;">संपर्क साधा / Get In Touch</h2>
            <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
                <a href="tel:{phone}" style="background: #222; color: #fff; padding: 12px 25px; border-radius: 8px; text-decoration: none; font-weight: bold;">📞 {phone}</a>
                <a href="https://wa.me/{clean_phone}?text=Hello%20{name}" target="_blank" style="background: #25D366; color: #fff; padding: 12px 25px; border-radius: 8px; text-decoration: none; font-weight: bold;">💬 WhatsApp Chat</a>
            </div>
        </div>
    </section>
    """
