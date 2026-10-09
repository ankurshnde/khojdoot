"""
Website Generation & Conversational Editing Routes.
Owner: Abhishek (Backend / FastAPI)
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.db.crud import get_shop_by_slug, get_latest_website_spec, get_bin, save_website_spec
from app.harness.workflow import execute_workflow
from app.website.patcher import patch_website_spec
from app.website.generator import generate_website
from app.validation.website import validate_website_html
from app.publishing.merchant_site import publish_merchant_html

router = APIRouter()


class EditInstruction(BaseModel):
    instruction: str


@router.post("/{slug}/generate")
def generate_merchant_website(slug: str):
    """Triggers Checkpoint 2 website generation."""
    result = execute_workflow({"slug": slug, "phase": "checkpoint2"})

    shop = get_shop_by_slug(slug)
    if shop and result.get("website_spec"):
        save_website_spec(shop["id"], version=1, spec_data=result["website_spec"])

    return {
        "status": "success",
        "checkpoint": "CHECKPOINT_2_PREVIEW_READY",
        "data": result,
    }



@router.post("/{slug}/edit")
def edit_merchant_website(slug: str, edit: EditInstruction):
    """Conversational natural-language editing on Checkpoint 2 preview."""
    shop = get_shop_by_slug(slug)
    if not shop:
        raise HTTPException(status_code=404, detail="Shop not found")

    spec = get_latest_website_spec(shop["id"]) or {"theme": {"style": "traditional"}, "version": 1}
    patched_spec = patch_website_spec(spec, edit.instruction)

    infobin = get_bin(shop["id"], "infobin") or {"name": shop["name"], "phone": shop["phone"], "location": shop["city"]}
    html = generate_website(patched_spec, infobin)
    scorecard = validate_website_html(html)

    return {
        "status": "patched",
        "spec": patched_spec,
        "scorecard": scorecard,
        "preview_html": html,
    }


@router.post("/{slug}/publish")
def publish_website(slug: str):
    """Publishes website and machine-readable assets."""
    shop = get_shop_by_slug(slug)
    if not shop:
        raise HTTPException(status_code=404, detail="Shop not found")

    spec = get_latest_website_spec(shop["id"]) or {"theme": {"style": "traditional"}}
    infobin = get_bin(shop["id"], "infobin") or {"name": shop["name"], "phone": shop["phone"], "location": shop["city"]}

    path = publish_merchant_html(slug, spec, infobin)
    return {
        "status": "published",
        "url": f"/merchant/{slug}",
        "file": path,
    }
