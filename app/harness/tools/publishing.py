"""Publishing Tool."""
from app.publishing.merchant_site import publish_merchant_html

def tool_publish_assets(slug: str, spec: dict, infobin: dict):
    return publish_merchant_html(slug, spec, infobin)
