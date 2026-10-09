"""
OpenRouter Client for Coding & Spec Customization.
Model: google/gemma-4-31b-it:free (with auto fallback to openrouter/free)
Owner: Ankur / Architecture
"""
import os
import json
import logging
from typing import Dict, Any, Optional
import httpx
from app.config import settings

logger = logging.getLogger(__name__)

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"


class OpenRouterClient:
    """Client for OpenRouter API optimized for Google Gemma models."""

    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        self.api_key = api_key or getattr(settings, "OPENROUTER_API_KEY", "") or os.getenv("OPENROUTER_API_KEY", "")
        self.primary_model = model or getattr(settings, "OPENROUTER_CODING_MODEL", "google/gemma-4-31b-it:free")
        self.fallback_model = "openrouter/free"

    async def generate_completion(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.2,
        max_tokens: int = 4096,
    ) -> str:
        """
        Generates completion using Google Gemma via OpenRouter.
        Falls back to openrouter/free if rate-limited.
        """
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        headers = {
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/ankurshnde/khojdoot",
            "X-Title": "KhojDoot Regional Website Builder",
        }
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        models_to_try = [self.primary_model, self.fallback_model]

        async with httpx.AsyncClient(timeout=45.0) as client:
            for model_name in models_to_try:
                payload = {
                    "model": model_name,
                    "messages": messages,
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                }
                try:
                    response = await client.post(OPENROUTER_API_URL, headers=headers, json=payload)
                    if response.status_code == 200:
                        data = response.json()
                        choices = data.get("choices", [])
                        if choices:
                            return choices[0].get("message", {}).get("content", "")
                    else:
                        logger.warning(
                            f"OpenRouter model {model_name} returned status {response.status_code}: {response.text}"
                        )
                except Exception as e:
                    logger.warning(f"Failed to query OpenRouter model {model_name}: {e}")

        return ""

    def generate_completion_sync(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.2,
        max_tokens: int = 4096,
    ) -> str:
        """Synchronous wrapper for graph nodes."""
        import asyncio
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                import nest_asyncio
                nest_asyncio.apply()
                return loop.run_until_complete(
                    self.generate_completion(prompt, system_prompt, temperature, max_tokens)
                )
            else:
                return loop.run_until_complete(
                    self.generate_completion(prompt, system_prompt, temperature, max_tokens)
                )
        except Exception:
            # Fallback if asyncio event loop is already bound
            with httpx.Client(timeout=45.0) as client:
                headers = {
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://github.com/ankurshnde/khojdoot",
                    "X-Title": "KhojDoot Regional Website Builder",
                }
                if self.api_key:
                    headers["Authorization"] = f"Bearer {self.api_key}"
                for model_name in [self.primary_model, self.fallback_model]:
                    payload = {
                        "model": model_name,
                        "messages": [
                            *([{"role": "system", "content": system_prompt}] if system_prompt else []),
                            {"role": "user", "content": prompt},
                        ],
                        "temperature": temperature,
                        "max_tokens": max_tokens,
                    }
                    try:
                        res = client.post(OPENROUTER_API_URL, headers=headers, json=payload)
                        if res.status_code == 200:
                            data = res.json()
                            choices = data.get("choices", [])
                            if choices:
                                return choices[0].get("message", {}).get("content", "")
                    except Exception as err:
                        logger.warning(f"Sync OpenRouter fallback exception: {err}")
        return ""


openrouter_client = OpenRouterClient()
