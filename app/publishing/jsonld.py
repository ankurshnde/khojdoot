"""Schema.org JSON-LD Structured Data."""
import json
from typing import Dict, Any


def generate_json_ld(infobin: Dict[str, Any]) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": infobin.get("name"),
        "telephone": infobin.get("phone"),
        "address": {
            "@type": "PostalAddress",
            "streetAddress": infobin.get("location"),
        },
    }
    return f'<script type="application/ld+json">\n{json.dumps(data, indent=2, ensure_ascii=False)}\n</script>'
