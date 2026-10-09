
from fastapi import APIRouter, Depends, HTTPException

from app.schemas.website import GenerateRequest, GenerateResponse
from app.services.generator import generate_website
from app.routes.auth import get_current_user

router = APIRouter(
    prefix="/api/v1",
    tags=["Website Generation"],
)


@router.post("/generate", response_model=GenerateResponse)
def generate(
    request: GenerateRequest,
    user=Depends(get_current_user),
):
    try:
        return generate_website(request)

    except RuntimeError as exc:
        message = str(exc)

        if "SARVAM_API_KEY is missing" in message:
            raise HTTPException(
                status_code=503,
                detail="AI service is not configured.",
            ) from exc

        raise HTTPException(
            status_code=502,
            detail="Website generation failed. Please try again.",
        ) from exc
