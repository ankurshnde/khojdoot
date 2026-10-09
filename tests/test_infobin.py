"""Unit tests for InfoBin & Pydantic Validation."""
import pytest
from app.schemas.infobin import InfoBin, MenuItem
from app.validation.business import validate_infobin


def test_infobin_creation_and_validation():
    bin_data = InfoBin(
        name="Sunita Tiffin Service",
        category="home_food",
        location="Gangapur Road, Nashik",
        phone="+91 9423375197",
        services="Homemade Veg Tiffin",
        menu=[MenuItem(item="साधा टिफिन", price=80.0)],
        hours="11:00 AM - 3:00 PM",
    )
    result = validate_infobin(bin_data)
    assert result["valid"] is True
    assert result["score"] == 1.0
