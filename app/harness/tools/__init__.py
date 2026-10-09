"""
LangChain / LangGraph Agent Tools Package.
Owner: Ankur (Architecture Lead)
Exposes typed, schema-validated tools for Agent Harness graph nodes.
"""
from typing import Dict, Any, List, Optional
from langchain_core.tools import tool
from app.db.crud import (
    create_or_update_shop,
    get_shop_by_slug,
    save_bin,
    get_bin,
    save_website_spec,
    get_latest_website_spec,
)
from app.website.generator import generate_website
from app.validation.website import validate_website_html
from app.publishing.merchant_site import publish_merchant_html


@tool
def lookup_merchant_profile(slug: str) -> Dict[str, Any]:
    """Retrieves existing merchant shop profile and verified facts by slug."""
    shop = get_shop_by_slug(slug)
    if not shop:
        return {"found": False, "slug": slug}
    infobin = get_bin(shop["id"], "infobin") or {}
    spec = get_latest_website_spec(shop["id"]) or {}
    return {
        "found": True,
        "shop": dict(shop),
        "infobin": infobin,
        "website_spec": spec,
    }


@tool
def persist_merchant_infobin(slug: str, name: str, phone: str, location: str, infobin: Dict[str, Any]) -> Dict[str, Any]:
    """Persists or updates merchant facts into the InfoBin database table."""
    sme_id = f"sme_{slug}"
    shop_id = create_or_update_shop(sme_id=sme_id, slug=slug, name=name, phone=phone, city=location)
    save_bin(shop_id=shop_id, bin_type="infobin", data=infobin)
    return {"shop_id": shop_id, "slug": slug, "saved": True}


@tool
def render_and_validate_website(spec: Dict[str, Any], infobin: Dict[str, Any]) -> Dict[str, Any]:
    """Renders semantic HTML from WebsiteSpec and runs the 8-point deterministic validator."""
    html = generate_website(spec, infobin)
    scorecard = validate_website_html(html)
    return {
        "html_length": len(html),
        "validation_passed": scorecard.get("passed", False),
        "scorecard": scorecard,
    }


@tool
def publish_discoverable_assets(slug: str, spec: Dict[str, Any], infobin: Dict[str, Any]) -> Dict[str, Any]:
    """Publishes static HTML and complete crawlable machine-readable assets bundle."""
    index_path = publish_merchant_html(slug, spec, infobin)
    return {
        "slug": slug,
        "index_file": index_path,
        "live_url": f"/merchant/{slug}",
        "assets": [
            f"/merchant/{slug}",
            f"/merchant/{slug}/facts.json",
            f"/merchant/{slug}/agentfacts.json",
            f"/merchant/{slug}/llms.txt",
            f"/merchant/{slug}/llms-full.txt",
            f"/merchant/{slug}/robots.txt",
            f"/merchant/{slug}/sitemap.xml",
        ],
    }


HARNESS_TOOLS = [
    lookup_merchant_profile,
    persist_merchant_infobin,
    render_and_validate_website,
    publish_discoverable_assets,
]
