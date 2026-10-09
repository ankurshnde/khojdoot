"""
Merchant & Web Chat Routes.
Owner: Abhishek (Backend / FastAPI)
"""
import os
import shutil
from datetime import datetime
from typing import Optional, List
from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from pydantic import BaseModel, Field

from app.config import settings
from app.db.crud import (
    create_or_update_shop,
    get_shop_by_slug,
    save_bin,
    get_bin,
    save_consent,
    save_photo,
)
from app.harness.workflow import execute_workflow
from app.ai.sarvam import transcribe_audio

router = APIRouter()


class ChatInput(BaseModel):
    message: str = Field(..., description="Merchant text message in regional language or English")
    language: Optional[str] = Field("mr-IN", description="Regional language code (e.g. mr-IN, hi-IN, en-IN)")


class ApprovalPayload(BaseModel):
    approved: bool = Field(..., description="Whether merchant approves extracted business facts")
    corrections: Optional[str] = Field(None, description="Optional corrections if not approved")


@router.get("/{slug}")
def get_merchant_details(slug: str):
    """Retrieves existing merchant shop record and extracted infobin."""
    shop = get_shop_by_slug(slug)
    if not shop:
        raise HTTPException(status_code=404, detail=f"Merchant with slug '{slug}' not found.")

    infobin = get_bin(shop["id"], "infobin")
    return {
        "status": "success",
        "shop": shop,
        "infobin": infobin,
    }


@router.post("/{slug}/chat")
def chat_with_merchant(slug: str, chat: ChatInput):
    """Processes Web Chat requirement input for Checkpoint 1."""
    if not chat.message or not chat.message.strip():
        raise HTTPException(status_code=400, detail="Chat message cannot be empty.")

    try:
        result = execute_workflow({"slug": slug, "raw_input": chat.message.strip(), "phase": "checkpoint1"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Workflow processing error: {str(e)}")

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
        "slug": slug,
        "data": result,
    }


@router.post("/{slug}/voice")
async def ingest_merchant_voice(
    slug: str,
    file: UploadFile = File(..., description="Audio file (.wav or .ogg)"),
    language: Optional[str] = Form("mr-IN", description="Audio language code (default: mr-IN)"),
):
    """
    Voice Note Ingestion Endpoint.
    Receives .wav or .ogg regional audio notes, transcribes via Sarvam AI,
    and runs Checkpoint 1 requirement extraction.
    """
    filename = file.filename or "recording.wav"
    ext = os.path.splitext(filename)[1].lower()
    allowed_extensions = {".wav", ".ogg", ".mp3", ".m4a"}

    if ext not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported audio format '{ext}'. Supported formats: {', '.join(sorted(allowed_extensions))}",
        )

    # Persist audio file to upload directory
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    safe_filename = f"{slug}_voice_{timestamp}{ext}"
    filepath = os.path.join(settings.UPLOAD_DIR, safe_filename)

    try:
        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save audio file: {str(e)}")

    # Transcribe audio via Sarvam Saaras API
    try:
        transcript = await transcribe_audio(filepath, language_code=language or "mr-IN")
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Audio transcription service failed: {str(e)}")

    if not transcript or not transcript.strip():
        raise HTTPException(
            status_code=422,
            detail="Transcription returned empty text. Please record a clearer voice note.",
        )

    # Run Checkpoint 1 extraction workflow
    try:
        result = execute_workflow({"slug": slug, "raw_input": transcript.strip(), "phase": "checkpoint1"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Workflow processing error: {str(e)}")

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
        "slug": slug,
        "audio_file": safe_filename,
        "transcript": transcript,
        "data": result,
    }


@router.post("/{slug}/checkpoint1/approve")
def approve_checkpoint1(slug: str, payload: ApprovalPayload):
    """Checkpoint 1: Merchant reviews and approves extracted business facts."""
    shop = get_shop_by_slug(slug)
    if not shop:
        raise HTTPException(status_code=404, detail=f"Merchant with slug '{slug}' not found.")

    if not payload.approved:
        return {
            "status": "rejected",
            "message": "Corrections requested",
            "corrections": payload.corrections,
            "slug": slug,
        }

    save_consent(shop["id"], consent_type="checkpoint1_business_info")

    return {
        "status": "approved",
        "message": "Checkpoint 1 approved. Website generation unlocked.",
        "slug": slug,
        "next": f"/api/website/{slug}/generate",
    }


@router.post("/{slug}/photos")
async def upload_merchant_photo(slug: str, file: UploadFile = File(...)):
    """Upload photo (rate card / menu) for merchant."""
    shop = get_shop_by_slug(slug)
    if not shop:
        raise HTTPException(status_code=404, detail=f"Merchant with slug '{slug}' not found.")

    filename = file.filename or "photo.jpg"
    ext = os.path.splitext(filename)[1].lower()
    allowed_extensions = {".jpg", ".jpeg", ".png", ".webp"}

    if ext not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported photo format '{ext}'. Supported formats: {', '.join(sorted(allowed_extensions))}",
        )

    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    saved_filename = f"{shop['id']}_{datetime.now().strftime('%Y%m%d%H%M%S')}_{filename}"
    filepath = os.path.join(settings.UPLOAD_DIR, saved_filename)

    try:
        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save photo: {str(e)}")

    save_photo(shop["id"], saved_filename)
    return {"status": "success", "filename": saved_filename, "slug": slug}

