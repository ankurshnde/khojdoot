"""LLMs.txt and LLMs-Full.txt Context Generator."""
from typing import Dict, Any


def generate_llms_txt(infobin: Dict[str, Any]) -> str:
    name = infobin.get("name", "Business")
    services = infobin.get("services", "")
    phone = infobin.get("phone", "")
    loc = infobin.get("location", "")
    return f"""# {name}
> {services}

## Details
- Location: {loc}
- Contact: {phone}
- Verified by KhojDoot
"""


def generate_llms_full_txt(infobin: Dict[str, Any]) -> str:
    base = generate_llms_txt(infobin)
    menu_items = "\n".join([f"- {m.get('item')}: ₹{m.get('price', '')}" for m in infobin.get("menu", [])])
    return f"""{base}

## Full Offerings & Menu
{menu_items}
"""
