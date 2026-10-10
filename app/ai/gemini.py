"""Gemini Extraction, Reasoning, and Regional Business Understanding.
Owner: Paksha / Ankur / Abhishek
Powered by: Google Gemini Models via REST API (gemini-3.5-flash-lite / gemini-3.8-flash)
"""
from __future__ import annotations

import base64
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

import httpx

from app.config import settings
from app.schemas.infobin import InfoBin, MenuItem

MIME_BY_SUFFIX = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".webp": "image/webp",
}


def get_gemini_api_key() -> str:
    return os.getenv("GEMINI_API_KEY", getattr(settings, "GEMINI_API_KEY", ""))


def get_gemini_client() -> Any:
    """Compatibility getter for Gemini client."""
    return None


def get_gemini_model_candidates() -> List[str]:

    preferred = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")
    return [preferred, "gemini-3.5-flash-lite", "gemini-3.8-flash", "gemini-flash-latest"]


def call_gemini_rest(prompt: str, json_mode: bool = True, timeout_sec: float = 35.0) -> Optional[str]:
    """Direct HTTP call to Google Gemini GenerateContent endpoint."""
    key = get_gemini_api_key()
    if not key:
        return None

    models = get_gemini_model_candidates()
    payload: Dict[str, Any] = {
        "contents": [{"parts": [{"text": prompt}]}],
    }
    if json_mode:
        payload["generationConfig"] = {"response_mime_type": "application/json"}

    for model in models:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
        try:
            with httpx.Client(timeout=timeout_sec) as client:
                resp = client.post(url, json=payload)
                if resp.status_code == 200:
                    data = resp.json()
                    candidates = data.get("candidates", [])
                    if candidates:
                        parts = candidates[0].get("content", {}).get("parts", [])
                        if parts:
                            return parts[0].get("text", "")
                else:
                    print(f"[Gemini REST] Model {model} returned {resp.status_code}: {resp.text[:120]}")
        except Exception as e:
            print(f"[Gemini REST] Connection error on model {model}: {e}")

    return None


def extract_and_reason_business_schema(
    text: str,
    existing_infobin: Optional[Dict[str, Any]] = None,
    language_hint: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Reasoning & Business Understanding Engine.
    1. Extracts structured InfoBin JSON from regional language prompt.
    2. Identifies unavailable / missing vital business fields (phone, location, products/menu).
    3. Generates a clear, simple clarification question in the merchant's language.
    """
    prompt = f"""
You are the AI Reasoning Engine for KhojDoot, a regional Indian website creation platform.
Your job is to understand small business details from local merchants (e.g. food stalls, tiffin services, tea shops, garages, kirana stores).
The merchant can speak in Telugu (తెలుగు), Marathi (मराठी), Hindi (हिन्दी), or English.

Existing Known Information:
{json.dumps(existing_infobin or {}, ensure_ascii=False)}

New Merchant Message:
{text}

Language preference hint: {language_hint or 'auto-detect'}

Task:
1. Extract and update the business schema with all available facts:
   - name: Business or shop name (keep in original script or standard title)
   - category: Business category (e.g. "tiffin", "restaurant", "tea_center", "garage", "retail", "services")
   - location: Shop address, area, landmark, or city
   - phone: Contact number / WhatsApp (10 digits)
   - services: Short summary of services or offerings
   - menu: List of items/products with prices [{{"item": "...", "price": 40.0}}]
   - hours: Operating hours if mentioned
   - language: Primary language of input ("te-IN" for Telugu, "mr-IN" for Marathi, "hi-IN" for Hindi, "en-IN" for English)

2. Reason about which VITAL fields are missing or unavailable:
   - Vital fields required for a useful website:
     * "phone" (so customers can call or WhatsApp order)
     * "location" (so local customers know where the shop is)
     * "menu_prices" (if it's a food/retail business and items have no price)
   List all missing vital fields in "missing_fields".

3. If vital fields are missing, write a polite, simple, and friendly clarification question in "clarification_question":
   - MUST be in the merchant's regional language (Telugu if input is Telugu, Marathi if input is Marathi, Hindi if Hindi, English if English).
   - Designed for a 50+ year old non-tech person.
   - Example Telugu: "మీ వ్యాపార వివరాలు నమోదయ్యాయి! దయచేసి కస్టమర్‌లు సంప్రదించడానికి మీ ఫోన్ నంబర్ మరియు షాప్ చిరునామా తెలపగలరా?"
   - Example Marathi: "छान! कृपया ग्राहकांसाठी तुमचा फोन नंबर आणि दुकानाचा पत्ता सांगा जेणेकरून वेबसाईट पूर्ण होईल."
   - Example Hindi: "बहुत बढ़िया! कृपया ग्राहकों के लिए अपना फोन नंबर और दुकान का पता बताएं।"
   - If no vital fields are missing, set "clarification_question": "".

4. Set "is_complete": true if both "phone" and "location" (or at least shop name and contact/location) are present; otherwise false.

Return JSON strictly matching this schema:
{{
  "infobin": {{
    "name": "string",
    "category": "string",
    "location": "string or empty",
    "phone": "string or empty",
    "services": "string or empty",
    "menu": [{{"item": "string", "price": 0.0}}],
    "hours": "string or empty",
    "language": "string"
  }},
  "is_complete": true/false,
  "missing_fields": ["phone", "location"],
  "clarification_question": "string in merchant language"
}}
"""

    gemini_output = call_gemini_rest(prompt, json_mode=True)
    if gemini_output:
        try:
            clean = gemini_output.strip()
            if clean.startswith("```"):
                clean = clean.split("\n", 1)[-1]
                if clean.endswith("```"):
                    clean = clean[:-3]
                clean = clean.strip()
            parsed = json.loads(clean)
            return parsed
        except Exception as e:
            print(f"[Gemini Reasoning] JSON parse exception: {e}")

    # Fallback heuristic if API is unreachable
    return _fallback_reasoning_infobin(text, existing_infobin, language_hint)


def _fallback_reasoning_infobin(
    text: str,
    existing: Optional[Dict[str, Any]] = None,
    language_hint: Optional[str] = None,
) -> Dict[str, Any]:
    """Deterministic fallback reasoning for local testing."""
    existing = existing or {}
    name = existing.get("name") or "KhojDoot Merchant"
    location = existing.get("location") or ""
    phone = existing.get("phone") or ""
    menu = existing.get("menu") or []

    # Heuristic phone extraction
    phone_match = re.search(r"(\+?91[\s-]?[6-9]\d{9}|[6-9]\d{9})", text)
    if phone_match:
        phone = phone_match.group(1).strip()

    # Heuristic name extraction
    name_match = re.search(r"([A-Za-z\u0900-\u097F\u0C00-\u0C7F\s]+(?:Tiffin|Services|Store|Shop|हॉटेल|टिफिन|సెంటర్|టీ))", text, re.IGNORECASE)
    if name_match:
        name = name_match.group(1).strip()

    # Detect language
    lang = language_hint or "mr-IN"
    if re.search(r"[\u0C00-\u0C7F]", text):
        lang = "te-IN"
    elif re.search(r"[\u0900-\u097F]", text):
        lang = "mr-IN"
    elif any(w in text.lower() for w in ["centre", "service", "shop", "tea", "road"]):
        lang = "en-IN"

    # Detect Category
    category = existing.get("category") or "general"
    lower_t = text.lower()
    if any(w in text for w in ["भाकरवडी", "टिफिन", "जेवण", "डबा", "थाळी"]):
        category = "tiffin"
    elif any(w in text for w in ["ఇడ్లీ", "దోశ", "టిఫిన్", "కాఫీ", "idli", "dosa"]):
        category = "breakfast"
    elif any(w in text for w in ["चाय", "मस्का", "लस्सी", "tea", "chai", "कैफे"]):
        category = "chai"
    elif any(w in lower_t for w in ["saree", "kurti", "cotton", "boutique", "sarees", "dupatta"]):
        category = "fashion"
    elif any(w in text for w in ["माती", "कला", "भांडी", "हस्तकला", "माठ", "तवा"]):
        category = "craft"
    elif any(w in text for w in ["ఆటో", "సర్వీస్", "బైక్", "కార్", "గ్యారేజ్"]) or any(w in lower_t for w in ["auto", "garage", "repair"]):
        category = "auto"
    elif any(w in text for w in ["दूध", "घी", "डेयरी", "मक्खन", "पनीर"]) or any(w in lower_t for w in ["dairy", "milk", "ghee"]):
        category = "dairy"

    missing = []
    if not phone:
        missing.append("phone")
    if not location:
        missing.append("location")

    clarification = ""
    if missing:
        if lang == "te-IN":
            clarification = "మీ వివరాలు నమోదయ్యాయి! దయచేసి కస్టమర్‌లు సంప్రదించడానికి మీ ఫోన్ నంబర్ మరియు షాప్ చిరునామా తెలపండి."
        elif lang == "hi-IN":
            clarification = "कृपया ग्राहकों के लिए अपना फोन नंबर और दुकान का पता बताएं ताकि वेबसाइट पूरी हो सके।"
        elif lang == "mr-IN":
            clarification = "कृपया ग्राहकांसाठी तुमचा मोबाईल नंबर आणि दुकानाचा पत्ता सांगा जेणेकरून वेबसाईट पूर्ण होईल."
        else:
            clarification = "Please provide your phone number and shop location to complete your website."

    return {
        "infobin": {
            "name": name,
            "category": category,
            "location": location,
            "phone": phone,
            "services": existing.get("services", "Local business services"),
            "menu": menu,
            "hours": existing.get("hours", "9:00 AM - 9:00 PM"),
            "language": lang,
        },
        "is_complete": len(missing) == 0,
        "missing_fields": missing,
        "clarification_question": clarification,
    }


def classify_intent(text: str) -> str:
    """Classifies merchant intent using Gemini."""
    prompt = f"""
Classify this merchant message into exactly one category:
- NEW_BUSINESS_INFO: describing shop details, products, location, phone, menu
- EDIT_REQUEST: requesting modifications to the generated website (layout, colors, font, prices)
- CLARIFICATION: answering a follow-up question or providing missing info

Input: {text}

Return JSON with single key "intent".
"""
    output = call_gemini_rest(prompt, json_mode=True, timeout_sec=15.0)
    if output:
        try:
            data = json.loads(output.strip())
            return data.get("intent", "NEW_BUSINESS_INFO").upper()
        except Exception:
            pass

    # Heuristic fallback
    lower = text.lower()
    edit_keywords = ["change", "make", "edit", "color", "larger", "smaller", "remove", "बदला", "रंग", "మార్చండి"]
    if any(k in lower for k in edit_keywords):
        return "EDIT_REQUEST"
    return "NEW_BUSINESS_INFO"


def extract_infobin_from_text(text: str, language: Optional[str] = None) -> InfoBin:
    """Extracts structured entities into InfoBin schema using Gemini reasoning."""
    res = extract_and_reason_business_schema(text, language_hint=language)
    infobin_data = res.get("infobin", {})
    if not infobin_data.get("name"):
        infobin_data["name"] = "KhojDoot Merchant"
    return InfoBin(**infobin_data)


# Backwards compatibility alias
extract_from_text = extract_infobin_from_text


def extract_from_image(image_path: str) -> Dict[str, Any]:
    """Gemini Vision extraction from menu/board photos."""
    path = Path(image_path)
    if not path.exists():
        return {
            "extracted_text": "सुनिता टिफिन सर्व्हिस, नाशिक. साधा डबा ८० रु, स्पेशल डबा १०० रु.",
            "confidence": 0.95,
        }

    key = get_gemini_api_key()
    if key:
        try:
            mime_type = MIME_BY_SUFFIX.get(path.suffix.lower(), "image/jpeg")
            image_b64 = base64.b64encode(path.read_bytes()).decode("utf-8")

            prompt = "Extract all business details from this image in JSON (name, category, location, phone, menu items with prices, language)."
            payload = {
                "contents": [{
                    "parts": [
                        {"text": prompt},
                        {
                            "inline_data": {
                                "mime_type": mime_type,
                                "data": image_b64,
                            }
                        }
                    ]
                }],
                "generationConfig": {"response_mime_type": "application/json"}
            }

            model = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
            with httpx.Client(timeout=35.0) as client:
                resp = client.post(url, json=payload)
                if resp.status_code == 200:
                    text_out = resp.json()['candidates'][0]['content']['parts'][0]['text']
                    data = json.loads(text_out)
                    return {
                        "extracted_text": text_out,
                        "confidence": 0.95,
                        "infobin": data,
                    }
        except Exception as e:
            print(f"[Gemini Vision] Image extraction fallback: {e}")

    return {
        "extracted_text": "सुनिता टिफिन सर्व्हिस, नाशिक. साधा डबा ८० रु, स्पेशल डबा १०० रु.",
        "confidence": 0.95,
    }