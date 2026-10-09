"""
Published Assets & Agentic Web Routes.
Owner: Abhishek / Ankur
"""
from fastapi import APIRouter, Response, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
from app.db.crud import get_shop_by_slug, get_latest_website_spec, get_bin
from app.website.generator import generate_website
from app.publishing.agentfacts import generate_agentfacts
from app.publishing.agent_card import generate_agent_card
from app.publishing.business_json import generate_business_json
from app.publishing.llms import generate_llms_txt, generate_llms_full_txt
from app.publishing.sitemap import generate_sitemap
from app.publishing.robots import generate_robots_txt

router = APIRouter()


@router.get("/merchant/{slug}", response_class=HTMLResponse)
def view_merchant_website(slug: str):
    shop = get_shop_by_slug(slug)
    if not shop:
        raise HTTPException(status_code=404, detail="Merchant not found")

    spec = get_latest_website_spec(shop["id"]) or {"theme": {"style": "traditional"}}
    infobin = get_bin(shop["id"], "infobin") or {"name": shop["name"], "phone": shop["phone"], "location": shop["city"]}
    return generate_website(spec, infobin)


@router.get("/merchant/{slug}/facts.json", response_class=JSONResponse)
def view_business_json(slug: str):
    shop = get_shop_by_slug(slug)
    if not shop:
        raise HTTPException(status_code=404, detail="Merchant not found")
    infobin = get_bin(shop["id"], "infobin") or {"name": shop["name"], "phone": shop["phone"], "location": shop["city"]}
    return generate_business_json(infobin)


@router.get("/merchant/{slug}/agentfacts.json", response_class=JSONResponse)
def view_agentfacts(slug: str):
    shop = get_shop_by_slug(slug)
    if not shop:
        raise HTTPException(status_code=404, detail="Merchant not found")
    infobin = get_bin(shop["id"], "infobin") or {"name": shop["name"], "phone": shop["phone"], "location": shop["city"]}
    return generate_agentfacts(infobin)


@router.get("/merchant/{slug}/llms.txt", response_class=PlainTextResponse)
def view_llms_txt(slug: str):
    shop = get_shop_by_slug(slug)
    if not shop:
        raise HTTPException(status_code=404, detail="Merchant not found")
    infobin = get_bin(shop["id"], "infobin") or {"name": shop["name"], "phone": shop["phone"], "location": shop["city"]}
    return generate_llms_txt(infobin)


@router.get("/.well-known/agent-card.json", response_class=JSONResponse)
def view_agent_card():
    return generate_agent_card({"name": "KhojDoot Network"})


@router.get("/sitemap.xml", response_class=Response)
def view_sitemap():
    return Response(content=generate_sitemap("sunita-tiffin-service"), media_type="application/xml")


@router.get("/robots.txt", response_class=PlainTextResponse)
def view_robots():
    return generate_robots_txt()
