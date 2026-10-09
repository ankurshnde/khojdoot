"""Merchant Site Publisher."""
import os
from typing import Dict, Any
from app.config import settings
from app.website.generator import generate_website


def publish_merchant_html(slug: str, spec: Dict[str, Any], infobin: Dict[str, Any]) -> str:
    html = generate_website(spec, infobin)
    out_dir = os.path.join(settings.GENERATED_DIR, slug)
    os.makedirs(out_dir, exist_ok=True)
    file_path = os.path.join(out_dir, "index.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    return file_path
