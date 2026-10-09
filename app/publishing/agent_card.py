"""Agent Card Publisher."""
import json
from typing import Dict, Any


def generate_agent_card(infobin: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "name": f"{infobin.get('name')} Agent",
        "description": f"AI Representation for {infobin.get('name')}",
        "url": f"/.well-known/agent-card.json",
        "skills": ["catalog_query", "order_inquiry", "hours_query"],
    }
