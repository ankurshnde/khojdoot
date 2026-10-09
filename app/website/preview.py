"""
Live Website Preview Helper.
Owner: Gayatri (Frontend / Preview)
"""
from typing import Dict, Any
from app.website.generator import generate_website


def get_preview_html(spec: Dict[str, Any], infobin: Dict[str, Any]) -> str:
    return generate_website(spec, infobin)
