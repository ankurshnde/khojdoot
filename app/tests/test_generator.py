
import json

import httpx
import pytest

from app.schemas.website import GenerateRequest
from app.services.generator import (
    InvalidAIResponseError,
    ProviderAuthenticationError,
    ProviderRateLimitError,
    ProviderTimeoutError,
    generate_website,
)


VALID_WEBSITE = {
    "name": "Test Coaching",
    "language": "mr",
    "theme": {"primaryColor": "#2563eb"},
    "navigation": [{"label": "Home", "href": "/"}],
    "pages": [
        {
            "id": "home",
            "title": "Home",
            "path": "/",
            "components": [
                {
                    "id": "hero",
                    "type": "heading",
                    "props": {"text": "Welcome"},
                }
            ],
        }
    ],
}


def mock_response(status_code, body):
    request = httpx.Request(
        "POST", "https://api.sarvam.ai/v1/chat/completions"
    )
    return httpx.Response(
        status_code,
        json=body,
        request=request,
    )


def test_successful_generation(monkeypatch):
    monkeypatch.setenv("SARVAM_API_KEY", "test-key")

    def fake_post(self, *args, **kwargs):
        return mock_response(
            200,
            {
                "choices": [
                    {
                        "message": {
                            "content": json.dumps(VALID_WEBSITE)
                        }
                    }
                ]
            },
        )

    monkeypatch.setattr(httpx.Client, "post", fake_post)

    result = generate_website(
        GenerateRequest(prompt="Create a Marathi coaching website")
    )

    assert result.status == "ready"
    assert result.website.name == "Test Coaching"
    assert result.project_id


def test_rate_limit_is_detected(monkeypatch):
    monkeypatch.setenv("SARVAM_API_KEY", "test-key")

    def fake_post(self, *args, **kwargs):
        return mock_response(429, {"error": "rate limited"})

    monkeypatch.setattr(httpx.Client, "post", fake_post)

    with pytest.raises(ProviderRateLimitError):
        generate_website(
            GenerateRequest(prompt="Create a website")
        )


def test_authentication_failure_is_detected(monkeypatch):
    monkeypatch.setenv("SARVAM_API_KEY", "test-key")

    def fake_post(self, *args, **kwargs):
        return mock_response(401, {"error": "unauthorized"})

    monkeypatch.setattr(httpx.Client, "post", fake_post)

    with pytest.raises(ProviderAuthenticationError):
        generate_website(
            GenerateRequest(prompt="Create a website")
        )


def test_invalid_ai_json_is_detected(monkeypatch):
    monkeypatch.setenv("SARVAM_API_KEY", "test-key")

    def fake_post(self, *args, **kwargs):
        return mock_response(
            200,
            {
                "choices": [
                    {"message": {"content": "not valid JSON"}}
                ]
            },
        )

    monkeypatch.setattr(httpx.Client, "post", fake_post)

    with pytest.raises(InvalidAIResponseError):
        generate_website(
            GenerateRequest(prompt="Create a website")
        )


def test_provider_timeout_is_detected(monkeypatch):
    monkeypatch.setenv("SARVAM_API_KEY", "test-key")

    def fake_post(self, *args, **kwargs):
        request = httpx.Request(
            "POST", "https://api.sarvam.ai/v1/chat/completions"
        )
        raise httpx.ReadTimeout("Timed out", request=request)

    monkeypatch.setattr(httpx.Client, "post", fake_post)

    with pytest.raises(ProviderTimeoutError):
        generate_website(
            GenerateRequest(prompt="Create a website")
        )
