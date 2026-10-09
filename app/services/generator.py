
import json
import os
from uuid import uuid4

import httpx
from dotenv import load_dotenv
from pydantic import ValidationError
from app.services.project_store import project_store

from app.schemas.website import (
    GenerateRequest,
    GenerateResponse,
    WebsiteSpec,
)

load_dotenv()

SARVAM_API_URL = "https://api.sarvam.ai/v1/chat/completions"


class GeneratorError(RuntimeError):
    """Base error for website generation."""


class ConfigurationError(GeneratorError):
    pass


class ProviderAuthenticationError(GeneratorError):
    pass


class ProviderRateLimitError(GeneratorError):
    pass


class ProviderTimeoutError(GeneratorError):
    pass


class ProviderUnavailableError(GeneratorError):
    pass


class InvalidAIResponseError(GeneratorError):
    pass


SYSTEM_PROMPT = """
You are the website requirement interpreter for KhojDoot,
a regional-language no-code website builder.

Convert the user's request into one valid JSON object describing
an editable website.

The JSON must have this structure:
{
  "name": "Website name",
  "language": "mr",
  "theme": {
    "primaryColor": "#2563eb",
    "fontFamily": "system-ui"
  },
  "navigation": [
    {"label": "Home", "href": "/"}
  ],
  "pages": [
    {
      "id": "home",
      "title": "Home",
      "path": "/",
      "components": [
        {
          "id": "hero-title",
          "type": "heading",
          "props": {"text": "Welcome", "level": 1}
        }
      ]
    }
  ]
}

Rules:
- Use the user's requested language for website content.
- If language is "auto", infer it from the user's request.
- Preserve native scripts, including Devanagari and Telugu.
- Understand mixed-language requests too.
- Generate appropriate pages, navigation and components.
- Supported component types: heading, text, image, button,
  form, navbar, footer, card.
- Every component must have a unique id within its page.
- Every page must have an id, title, path and components.
- Use valid internal paths beginning with /.
- Navigation hrefs must match generated page paths.
- Keep props as JSON objects.
- Use sensible defaults for unspecified design choices.
- Do not generate executable JavaScript or raw HTML.
- Return JSON only, without Markdown fences.
"""


def generate_website(
    request: GenerateRequest,
) -> GenerateResponse:
    api_key = os.getenv("SARVAM_API_KEY")
    model = os.getenv("SARVAM_MODEL", "sarvam-105b")

    if not api_key:
        raise ConfigurationError(
            "SARVAM_API_KEY is missing."
        )

    try:
        with httpx.Client(timeout=60.0) as client:
            response = client.post(
                SARVAM_API_URL,
                headers={
                    "api-subscription-key": api_key,
                    "Content-Type": "application/json",
                },
                json={
                    "model": model,
                    "messages": [
                        {
                            "role": "system",
                            "content": SYSTEM_PROMPT,
                        },
                        {
                            "role": "user",
                            "content": (
                                f"Requested language: {request.language}\n"
                                f"Website requirements: {request.prompt}"
                            ),
                        },
                    ],
                    "response_format": {"type": "json_object"},
                    "temperature": 0.2,
                    "max_tokens": 4000,
                    "reasoning_effort": None,
                },
            )

    except httpx.TimeoutException as exc:
        raise ProviderTimeoutError(
            "Sarvam API request timed out."
        ) from exc

    except httpx.RequestError as exc:
        raise ProviderUnavailableError(
            "Could not connect to Sarvam API."
        ) from exc

    if response.status_code in (401, 403):
        raise ProviderAuthenticationError(
            "Sarvam API authentication failed."
        )

    if response.status_code == 429:
        raise ProviderRateLimitError(
            "Sarvam API rate limit or quota reached."
        )

    if response.status_code >= 500:
        raise ProviderUnavailableError(
            "Sarvam API is temporarily unavailable."
        )

    if not response.is_success:
        raise GeneratorError(
            f"Sarvam API rejected the request "
            f"with status {response.status_code}."
        )

    try:
        result = response.json()
        content = result["choices"][0]["message"]["content"]

        if not isinstance(content, str):
            raise ValueError("AI response content must be text.")

        website_data = json.loads(content)
        website = WebsiteSpec.model_validate(website_data)

    except (
        ValueError,
        KeyError,
        IndexError,
        TypeError,
        ValidationError,
    ) as exc:
        raise InvalidAIResponseError(
            "Sarvam returned an invalid website specification."
        ) from exc

    project_id = str(uuid4())

    result = GenerateResponse(
        project_id=project_id,
        status="ready",
        website=website,
    )

    project_store.save(
        project_id,
        result.model_dump(mode="json"),
    )

    return result
