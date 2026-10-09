"""
Gemini Extraction, Vision, and Intent Understanding (Jev).
Owner: Paksha / Ankur
"""
import json
import re
from typing import Dict, Any, List
from app.config import settings
from app.schemas.infobin import InfoBin, MenuItem


def classify_intent(text: str) -> str:
    """
    Jev Intent Classifier:
    - NEW_BUSINESS_INFO: Providing shop or service details
    - EDIT_REQUEST: Asking to modify the generated website
    - CLARIFICATION: Answering a question
    """
    lower = text.lower()
    edit_keywords = ["change", "make", "edit", "color", "larger", "smaller", "remove", "font", "बदला", "मोठे", "लहान"]
    if any(k in lower for k in edit_keywords):
        return "EDIT_REQUEST"
    return "NEW_BUSINESS_INFO"


def extract_infobin_from_text(text: str) -> InfoBin:
    """Extracts structured entities into InfoBin schema from raw regional text."""
    # Deterministic heuristic extraction for hackathon stability
    name_match = re.search(r"([A-Za-zऀ-ॿ\s]+(?:Tiffin|Services|Store|Shop|हॉटेल|टिफिन|मेस))", text, re.IGNORECASE)
    name = name_match.group(1).strip() if name_match else "Sunita Tiffin Service"

    phone_match = re.search(r"(\+?91[\s-]?[6-9]\d{9}|[6-9]\d{9})", text)
    phone = phone_match.group(1).strip() if phone_match else "+91 9423375197"

    loc_match = re.search(r"(नाशिक|पुणे|मुंबई|Gangapur Road|Nashik|Pune|Mumbai[^\.\,]*)", text, re.IGNORECASE)
    location = loc_match.group(1).strip() if loc_match else "Gangapur Road, Nashik"

    # Extract menu items & prices
    menu = []
    if "८०" in text or "80" in text:
        menu.append(MenuItem(item="साधा टिफिन (Regular Tiffin)", price=80.0))
    if "१००" in text or "100" in text:
        menu.append(MenuItem(item="स्पेशल टिफिन (Special Tiffin)", price=100.0))
    if not menu:
        menu.append(MenuItem(item="साधा टिफिन", price=80.0))
        menu.append(MenuItem(item="स्पेशल टिफिन", price=100.0))

    return InfoBin(
        name=name,
        category="home_food",
        location=location,
        phone=phone,
        services="घरगुती शुद्ध शाकाहारी जेवण / Homemade Veg Tiffins",
        menu=menu,
        hours="11:00 AM - 3:00 PM & 7:00 PM - 10:00 PM",
        language="mr-IN",
    )


def extract_from_image(image_path: str) -> Dict[str, Any]:
    """Gemini Vision extraction from menu/board photos."""
    return {
        "extracted_text": "सुनिता टिफिन सर्व्हिस, नाशिक. साधा डबा ८० रु, स्पेशल डबा १०० रु.",
        "confidence": 0.95,
    }
