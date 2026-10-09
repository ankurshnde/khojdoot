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


@router.get("/merchant/{slug}/robots.txt", response_class=PlainTextResponse)
def view_merchant_robots(slug: str):
    return generate_robots_txt(base_url=f"http://localhost:8000/merchant/{slug}")


@router.get("/merchant/{slug}/sitemap.xml", response_class=Response)
def view_merchant_sitemap(slug: str):
    return Response(content=generate_sitemap(slug=slug), media_type="application/xml")


@router.get("/.well-known/agent-card.json", response_class=JSONResponse)
def view_agent_card():
    return generate_agent_card({"name": "KhojDoot Network"})


@router.get("/sitemap.xml", response_class=Response)
def view_sitemap():
    return Response(content=generate_sitemap("sunita-tiffin-service"), media_type="application/xml")


@router.get("/robots.txt", response_class=PlainTextResponse)
def view_robots():
    return generate_robots_txt()


# --- Frontend Templates & Legacy Compatibility Routes ---

def _render_template(filename: str) -> str:
    import os
    template_path = os.path.join(os.path.dirname(__file__), "..", "templates", filename)
    if os.path.exists(template_path):
        with open(template_path, "r", encoding="utf-8") as f:
            return f.read()
    raise HTTPException(status_code=404, detail=f"Template {filename} not found")


@router.get("/", response_class=HTMLResponse)
def view_index_hub():
    """Renders the main KhojDoot Feature Hub."""
    return _render_template("index.html")


@router.get("/login", response_class=HTMLResponse)
def view_login_page():
    """Renders the 10-digit mobile login and OTP gate."""
    return _render_template("login.html")


@router.get("/chat", response_class=HTMLResponse)
def view_chat_page():
    """Renders the conversational multimodal onboarding interface."""
    return _render_template("chat.html")


@router.get("/approval", response_class=HTMLResponse)
@router.get("/business-approval", response_class=HTMLResponse)
def view_approval_page():
    """Renders Checkpoint 1 business summary approval card."""
    return _render_template("approval.html")


@router.get("/preview", response_class=HTMLResponse)
@router.get("/website-preview", response_class=HTMLResponse)
def view_preview_page():
    """Renders Checkpoint 2 strictly gated preview."""
    return _render_template("preview.html")


@router.get("/editor", response_class=HTMLResponse)
@router.get("/edit-website", response_class=HTMLResponse)
def view_editor_page():
    """Renders the live split-screen conversational and voice website editor."""
    return _render_template("editor.html")


@router.get("/merchant/{slug}/card", response_class=HTMLResponse)
def view_khoj_card(slug: str):
    """Renders the visual Khoj Card template."""
    return _render_template("card.html")


@router.get("/labs", response_class=HTMLResponse)
def view_labs():
    """Renders the KhojDoot Labs telemetry dashboard."""
    return _render_template("labs.html")


@router.get("/upload", response_class=HTMLResponse)
def view_upload_form():
    """Renders the merchant shop upload form."""
    return _render_template("upload.html")



@router.get("/b/{slug}.json")
@router.get("/b/{slug}")
def get_public_b_shop(slug: str):
    """Compatibility route consumed by Khoj Card and external crawlers."""
    from app.db.crud import get_photos, get_facts
    shop = get_shop_by_slug(slug)
    if not shop:
        raise HTTPException(status_code=404, detail="Shop not found")

    facts = get_facts(shop["id"])
    photos = get_photos(shop["id"])

    return {
        "slug": shop["slug"],
        "name": shop["name"],
        "business_name": shop["name"],
        "city": shop["city"],
        "phone": shop["phone"],
        "status": shop.get("status", "draft"),
        "facts": facts,
        "photos": [dict(p) for p in photos],
    }

