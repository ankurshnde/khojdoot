"""
Merchant & Web Chat Routes.
Owner: Abhishek (Backend / FastAPI)
"""
from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import Optional, List
from app.db.crud import create_or_update_shop, get_shop_by_slug, save_bin, save_consent
from app.harness.workflow import execute_workflow

router = APIRouter()


class ChatInput(BaseModel):
    message: str
    language: Optional[str] = "mr-IN"


class ApprovalPayload(BaseModel):
    approved: bool
    corrections: Optional[str] = None


@router.post("/{slug}/chat")
def chat_with_merchant(slug: str, chat: ChatInput):
    """Processes Web Chat requirement input."""
    result = execute_workflow({"slug": slug, "raw_input": chat.message, "phase": "checkpoint1"})

    # Persist extracted facts to database
    infobin_data = result.get("infobin", {})
    name = infobin_data.get("name", slug.replace("-", " ").title())
    phone = infobin_data.get("phone", "")
    city = infobin_data.get("location", "")

    shop_id = create_or_update_shop(sme_id=f"sme_{slug}", slug=slug, name=name, phone=phone, city=city)
    save_bin(shop_id, "infobin", infobin_data)

    return {
        "status": "success",
        "checkpoint": "CHECKPOINT_1_AWAITING_APPROVAL",
        "data": result,
    }



@router.post("/{slug}/checkpoint1/approve")
def approve_checkpoint1(slug: str, payload: ApprovalPayload):
    """Checkpoint 1: Merchant reviews and approves extracted business facts."""
    if not payload.approved:
        return {"status": "rejected", "message": "Corrections requested", "corrections": payload.corrections}

    shop = get_shop_by_slug(slug)
    if shop:
        save_consent(shop["id"], consent_type="checkpoint1_business_info")

    return {
        "status": "approved",
        "message": "Checkpoint 1 approved. Website generation unlocked.",
        "next": f"/api/website/{slug}/generate",
    }


@router.post("/{slug}/photos")
async def upload_merchant_photo(slug: str, file: UploadFile = File(...)):
    """Upload photo (rate card / menu) for merchant."""
    import os, shutil
    from datetime import datetime
    from app.config import settings
    from app.db.crud import save_photo

    shop = get_shop_by_slug(slug)
    if not shop:
        raise HTTPException(status_code=404, detail="Shop not found")

    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    filename = f"{shop['id']}_{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}"
    filepath = os.path.join(settings.UPLOAD_DIR, filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    save_photo(shop["id"], filename)
    return {"status": "success", "filename": filename, "slug": slug}

