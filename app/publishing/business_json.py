"""Business JSON Publisher (/merchant/[slug]/facts.json)."""
import json
from typing import Dict, Any


def generate_business_json(infobin: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "slug": infobin.get("name", "").lower().replace(" ", "-"),
        "name": infobin.get("name"),
        "phone": infobin.get("phone"),
        "location": infobin.get("location"),
        "menu": infobin.get("menu", []),
        "hours": infobin.get("hours"),
    }
