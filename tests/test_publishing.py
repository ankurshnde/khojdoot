"""Unit tests for Agentic Web Asset publishing."""
from app.publishing.agentfacts import generate_agentfacts
from app.publishing.llms import generate_llms_txt


def test_agentic_assets():
    infobin = {"name": "Sunita Tiffin Service", "phone": "9423375197", "location": "Nashik"}
    facts = generate_agentfacts(infobin)
    assert facts["business_name"] == "Sunita Tiffin Service"

    llms = generate_llms_txt(infobin)
    assert "# Sunita Tiffin Service" in llms
