
from fastapi import APIRouter, HTTPException

from app.schemas.website import GenerateRequest, GenerateResponse
from app.services.generator import (
    ConfigurationError,
    GeneratorError,
    InvalidAIResponseError,
    ProviderAuthenticationError,
    ProviderRateLimitError,
    ProviderTimeoutError,
    ProviderUnavailableError,
    generate_website,
)

router = APIRouter(
    prefix="/api/v1",
    tags=["Website Generation"],
)


@router.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest):
    try:
        return generate_website(request)

    except ConfigurationError as exc:
        raise HTTPException(
            status_code=503,
            detail="AI service is not configured.",
        ) from exc

    except ProviderAuthenticationError as exc:
        raise HTTPException(
            status_code=502,
            detail="AI provider authentication failed.",
        ) from exc

    except ProviderRateLimitError as exc:
        raise HTTPException(
            status_code=429,
            detail="AI rate limit or quota reached. Try again later.",
        ) from exc

    except ProviderTimeoutError as exc:
        raise HTTPException(
            status_code=504,
            detail="AI provider timed out. Please try again.",
        ) from exc

    except ProviderUnavailableError as exc:
        raise HTTPException(
            status_code=503,
            detail="AI provider is temporarily unavailable.",
        ) from exc

    except InvalidAIResponseError as exc:
        raise HTTPException(
            status_code=502,
            detail="AI returned an invalid website specification.",
        ) from exc

    except GeneratorError as exc:
        raise HTTPException(
            status_code=502,
            detail="Website generation failed.",
        ) from exc
