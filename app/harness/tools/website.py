"""Website Tool."""
from app.website.generator import generate_website
from app.validation.website import validate_website_html

def tool_render_and_validate(spec: dict, infobin: dict):
    html = generate_website(spec, infobin)
    scorecard = validate_website_html(html)
    return {"html": html, "scorecard": scorecard}
