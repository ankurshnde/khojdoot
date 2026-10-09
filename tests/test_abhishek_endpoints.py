"""
Unit & Integration Tests for Abhishek's FastAPI Endpoints.
Covers:
- Auth & OTP (/api/auth/*)
- Merchant Chat, Voice Ingestion, Photos, Approvals (/api/merchants/*)
- Website Generation, Editing, Publishing (/api/website/*)
- Published Assets & Health Checks
"""
import io
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# --- Health & Root Tests ---

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "KhojDoot Backend"


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "health" in data


# --- Auth & OTP Tests ---

def test_send_and_verify_master_otp():
    phone = "9876543210"
    # Send OTP
    send_resp = client.post("/api/auth/send-otp", json={"mobile": phone})
    assert send_resp.status_code == 200
    send_data = send_resp.json()
    assert send_data["status"] == "success"
    assert send_data["user_id"] == phone
    assert send_data["master_demo_otp"] == "123456"

    # Verify with master OTP
    verify_resp = client.post("/api/auth/verify-otp", json={"mobile": phone, "otp": "123456"})
    assert verify_resp.status_code == 200
    verify_data = verify_resp.json()
    assert verify_data["status"] == "authenticated"
    assert verify_data["user_id"] == phone
    assert verify_data["access_token"] is not None


def test_send_and_verify_generated_otp():
    phone = "9123456789"
    send_resp = client.post("/api/auth/send-otp", json={"mobile": phone})
    assert send_resp.status_code == 200
    demo_otp = send_resp.json()["demo_otp"]

    # Verify with generated OTP
    verify_resp = client.post("/api/auth/verify-otp", json={"mobile": phone, "otp": demo_otp})
    assert verify_resp.status_code == 200
    assert verify_resp.json()["status"] == "authenticated"


def test_auth_invalid_mobile():
    response = client.post("/api/auth/send-otp", json={"mobile": "1234"})
    assert response.status_code == 400
    assert "Invalid mobile number" in response.json()["detail"]


def test_auth_wrong_otp():
    phone = "9988776655"
    client.post("/api/auth/send-otp", json={"mobile": phone})
    response = client.post("/api/auth/verify-otp", json={"mobile": phone, "otp": "000000"})
    assert response.status_code == 400
    assert "Invalid OTP code" in response.json()["detail"]


def test_auth_status_check():
    phone = "9876501234"
    client.post("/api/auth/send-otp", json={"mobile": phone})
    response = client.get(f"/api/auth/status/{phone}")
    assert response.status_code == 200
    assert response.json()["has_pending_otp"] is True


# --- Merchant & Chat Tests ---

def test_merchant_chat_success():
    slug = "sunita-tiffin-test"
    payload = {
        "message": "आम्ही घरगुती डबा सेवा देतो नाशिक मध्ये. फोन ९८२२१२३४५६. साधा डबा ८० रुपये.",
        "language": "mr-IN",
    }
    response = client.post(f"/api/merchants/{slug}/chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["checkpoint"] == "CHECKPOINT_1_AWAITING_APPROVAL"
    assert "infobin" in data["data"]


def test_merchant_chat_empty_message():
    slug = "empty-chat-test"
    response = client.post(f"/api/merchants/{slug}/chat", json={"message": "   "})
    assert response.status_code == 400
    assert "cannot be empty" in response.json()["detail"]


def test_merchant_voice_upload_and_transcription():
    slug = "sunita-voice-test"
    # Create dummy audio file payload (.wav)
    dummy_wav_bytes = b"RIFF\x24\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x44\xac\x00\x00\x88\x58\x01\x00\x02\x00\x10\x00data\x00\x00\x00\x00"
    files = {"file": ("test_voice.wav", io.BytesIO(dummy_wav_bytes), "audio/wav")}
    data = {"language": "mr-IN"}

    response = client.post(f"/api/merchants/{slug}/voice", files=files, data=data)
    assert response.status_code == 200
    res_data = response.json()
    assert res_data["status"] == "success"
    assert res_data["checkpoint"] == "CHECKPOINT_1_AWAITING_APPROVAL"
    assert "transcript" in res_data
    assert "audio_file" in res_data
    assert "infobin" in res_data["data"]


def test_merchant_voice_invalid_extension():
    slug = "invalid-voice-test"
    files = {"file": ("notes.txt", io.BytesIO(b"Hello world"), "text/plain")}
    response = client.post(f"/api/merchants/{slug}/voice", files=files)
    assert response.status_code == 400
    assert "Unsupported audio format" in response.json()["detail"]


def test_merchant_details_retrieval():
    slug = "sunita-voice-test"
    response = client.get(f"/api/merchants/{slug}")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["shop"]["slug"] == slug


def test_merchant_details_not_found():
    response = client.get("/api/merchants/non-existent-shop-xyz")
    assert response.status_code == 404


def test_checkpoint1_approval_flow():
    slug = "sunita-tiffin-test"
    # Reject with corrections
    reject_resp = client.post(
        f"/api/merchants/{slug}/checkpoint1/approve",
        json={"approved": False, "corrections": "कृपया पत्ता बदला"},
    )
    assert reject_resp.status_code == 200
    assert reject_resp.json()["status"] == "rejected"
    assert reject_resp.json()["corrections"] == "कृपया पत्ता बदला"

    # Approve
    approve_resp = client.post(
        f"/api/merchants/{slug}/checkpoint1/approve",
        json={"approved": True},
    )
    assert approve_resp.status_code == 200
    assert approve_resp.json()["status"] == "approved"
    assert "generate" in approve_resp.json()["next"]


def test_merchant_photo_upload():
    slug = "sunita-tiffin-test"
    dummy_image = b"\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00`\x00`\x00\x00\xff\xdb\x00C\x00"
    files = {"file": ("rate_card.jpg", io.BytesIO(dummy_image), "image/jpeg")}
    response = client.post(f"/api/merchants/{slug}/photos", files=files)
    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_merchant_photo_invalid_type():
    slug = "sunita-tiffin-test"
    files = {"file": ("document.pdf", io.BytesIO(b"%PDF-1.4"), "application/pdf")}
    response = client.post(f"/api/merchants/{slug}/photos", files=files)
    assert response.status_code == 400
    assert "Unsupported photo format" in response.json()["detail"]


# --- Website Generation, Editing & Publishing Tests ---

def test_website_generation_flow():
    slug = "sunita-tiffin-test"
    response = client.post(f"/api/website/{slug}/generate")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["checkpoint"] == "CHECKPOINT_2_PREVIEW_READY"
    assert "website_spec" in data["data"]


def test_website_generation_merchant_not_found():
    response = client.post("/api/website/unknown-merchant-404/generate")
    assert response.status_code == 404


def test_website_edit_instruction():
    slug = "sunita-tiffin-test"
    edit_payload = {"instruction": "रंग भगवा करा आणि थाळीची किंमत १२० रुपये करा"}
    response = client.post(f"/api/website/{slug}/edit", json=edit_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "patched"
    assert "preview_html" in data
    assert "scorecard" in data


def test_website_edit_empty_instruction():
    slug = "sunita-tiffin-test"
    response = client.post(f"/api/website/{slug}/edit", json={"instruction": "   "})
    assert response.status_code == 400
    assert "cannot be empty" in response.json()["detail"]


def test_website_publish_and_public_assets():
    slug = "sunita-tiffin-test"
    # Publish
    pub_resp = client.post(f"/api/website/{slug}/publish")
    assert pub_resp.status_code == 200
    assert pub_resp.json()["status"] == "published"
    assert pub_resp.json()["url"] == f"/merchant/{slug}"

    # Verify public merchant website
    web_resp = client.get(f"/merchant/{slug}")
    assert web_resp.status_code == 200
    assert "<!DOCTYPE html>" in web_resp.text or "<html" in web_resp.text

    # Verify machine-readable facts
    facts_resp = client.get(f"/merchant/{slug}/facts.json")
    assert facts_resp.status_code == 200

    agentfacts_resp = client.get(f"/merchant/{slug}/agentfacts.json")
    assert agentfacts_resp.status_code == 200

    llms_resp = client.get(f"/merchant/{slug}/llms.txt")
    assert llms_resp.status_code == 200
