"""Unit tests for Website Generator & Validation Suite."""
from app.website.generator import generate_website
from app.validation.website import validate_website_html


def test_website_generation_and_validation():
    spec = {"theme": {"primary_color": "#E05A47"}}
    infobin = {
        "name": "Sunita Tiffin Service",
        "phone": "+91 9423375197",
        "location": "Nashik",
        "services": "Veg Tiffin",
        "menu": [{"item": "साधा टिफिन", "price": 80.0}],
    }
    html = generate_website(spec, infobin)
    assert "Sunita Tiffin Service" in html
    report = validate_website_html(html)
    assert report["passed"] is True
