"""Unit tests for AI modules (Gemini & Sarvam).
Owner: Paksha
"""
import pytest
from app.ai.gemini import classify_intent, extract_infobin_from_text, extract_from_image
from app.ai.sarvam import transcribe, transcribe_audio


def test_classify_intent():
    # New business info
    intent1 = classify_intent("माझे नाव सुनिता टिफिन सर्व्हिस आहे. नाशिक येथे आमची सोय आहे.")
    assert intent1 in {"NEW_BUSINESS_INFO", "CLARIFICATION"}

    # Edit request
    intent2 = classify_intent("रंग लाल करा आणि फॉन्ट मोठा करा.")
    assert intent2 == "EDIT_REQUEST"


def test_extract_infobin():
    text = "सुनिता टिफिन सर्व्हिस, नाशिक. साधा डबा ८० रु, स्पेशल डबा १०० रु. फोन 9423375197."
    infobin = extract_infobin_from_text(text)
    assert infobin.name != ""
    assert infobin.phone != ""
    assert len(infobin.menu) >= 1


@pytest.mark.asyncio
async def test_sarvam_transcription():
    # Test transcribe_audio fallback/mock execution
    transcript = await transcribe_audio("non_existent_or_mock.wav", language_code="mr-IN")
    assert isinstance(transcript, str)
    assert len(transcript) > 0


def test_extract_from_image_fallback():
    result = extract_from_image("data/samples/test_shop.jpg")
    assert "extracted_text" in result
    assert result["confidence"] > 0
