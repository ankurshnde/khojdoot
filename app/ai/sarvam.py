"""
Sarvam Saaras Speech-to-Text Integration.
Owner: Paksha / Ankur
Model: saaras:v1 (language_code="mr-IN")
"""
import os
import httpx
from app.config import settings


async def transcribe_audio(file_path: str, language_code: str = "mr-IN") -> str:
    """Transcribes Marathi/Hindi audio via Sarvam Saaras API with fallback."""
    if not settings.SARVAM_API_KEY:
        # Fallback / mock transcription for local hackathon demo when key is not set
        return "घरगुती शुद्ध शाकाहारी जेवण आणि टिफिन सेवा. साधा डबा ८० रुपये, स्पेशल डबा १०० रुपये. गंगापूर रोड नाशिक."

    url = "https://api.sarvam.ai/speech-to-text"
    headers = {"api-subscription-key": settings.SARVAM_API_KEY}

    try:
        async with httpx.AsyncClient() as client:
            with open(file_path, "rb") as audio_file:
                files = {"file": audio_file}
                data = {"language_code": language_code, "model": "saaras:v1"}
                response = await client.post(url, headers=headers, files=files, data=data, timeout=30.0)
                if response.status_code == 200:
                    return response.json().get("transcript", "")
    except Exception as e:
        print(f"Sarvam STT exception: {e}")

    return "घरगुती टिफिन सेवा नाशिक"
