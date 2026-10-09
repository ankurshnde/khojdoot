"""AgentFacts Schema Publisher."""
import json
from typing import Dict, Any


def generate_agentfacts(infobin: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "$schema": "https://agentfacts.org/v1/schema.json",
        "business_name": infobin.get("name"),
        "category": infobin.get("category"),
        "contact": {
            "phone": infobin.get("phone"),
            "location": infobin.get("location"),
        },
        "catalog": infobin.get("menu", []),
        "hours": infobin.get("hours"),
        "verified_by": "KhojDoot Regional Platform",
    }
