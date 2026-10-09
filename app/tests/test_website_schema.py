
import pytest
from pydantic import ValidationError

from app.schemas.website import WebsiteSpec


def valid_website():
    return {
        "name": "Test Website",
        "language": "mr",
        "navigation": [
            {"label": "Home", "href": "/"}
        ],
        "pages": [
            {
                "id": "home",
                "title": "Home",
                "path": "/",
                "components": [
                    {
                        "id": "hero",
                        "type": "heading",
                        "props": {"text": "Welcome"},
                    }
                ],
            }
        ],
    }


def test_valid_website_is_accepted():
    website = WebsiteSpec(**valid_website())
    assert website.name == "Test Website"


def test_empty_pages_are_rejected():
    data = valid_website()
    data["pages"] = []

    with pytest.raises(ValidationError):
        WebsiteSpec(**data)


def test_duplicate_component_ids_are_rejected():
    data = valid_website()
    data["pages"][0]["components"].append({
        "id": "hero",
        "type": "text",
        "props": {"text": "Duplicate"},
    })

    with pytest.raises(ValidationError):
        WebsiteSpec(**data)


def test_invalid_navigation_is_rejected():
    data = valid_website()
    data["navigation"] = [
        {"label": "Admission", "href": "/admission"}
    ]

    with pytest.raises(ValidationError):
        WebsiteSpec(**data)


def test_unsupported_component_type_is_rejected():
    data = valid_website()
    data["pages"][0]["components"][0]["type"] = "video"

    with pytest.raises(ValidationError):
        WebsiteSpec(**data)
