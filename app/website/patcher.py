import json
import logging
from typing import Dict, Any
from app.ai.openrouter import openrouter_client

logger = logging.getLogger(__name__)


def patch_website_spec(spec: Dict[str, Any], edit_instruction: str) -> Dict[str, Any]:
    """
    Translates regional/English natural language edit requests into WebsiteSpec updates.
    Uses Google Gemma 31B (via OpenRouter) with deterministic keyword fallback.
    """
    if not edit_instruction or not edit_instruction.strip():
        return spec

    # Prompt Google Gemma to perform precise spec diff
    system_prompt = (
        "You are an expert web UI architect for Indic/regional small businesses. "
        "You are given a current WebsiteSpec JSON and a merchant's natural-language change request "
        "(in Marathi, Hindi, or English). "
        "Return ONLY a valid JSON object representing the updated WebsiteSpec. "
        "Do not wrap in markdown or commentary."
    )
    user_prompt = (
        f"Current WebsiteSpec:\n{json.dumps(spec, ensure_ascii=False, indent=2)}\n\n"
        f"Merchant Edit Request: \"{edit_instruction}\"\n\n"
        "Return the updated WebsiteSpec JSON only."
    )

    try:
        raw_response = openrouter_client.generate_completion_sync(
            prompt=user_prompt,
            system_prompt=system_prompt,
            temperature=0.1,
        )
        if raw_response:
            clean_json = raw_response.strip()
            if clean_json.startswith("```json"):
                clean_json = clean_json[7:]
            if clean_json.startswith("```"):
                clean_json = clean_json[3:]
            if clean_json.endswith("```"):
                clean_json = clean_json[:-3]
            clean_json = clean_json.strip()
            updated_spec = json.loads(clean_json)
            if isinstance(updated_spec, dict) and "theme" in updated_spec:
                updated_spec["version"] = spec.get("version", 1) + 1
                return updated_spec
    except Exception as e:
        logger.warning(f"Gemma spec patch failed, using fallback: {e}")

    # Deterministic fallback heuristics
    instruction_lower = edit_instruction.lower()
    if "theme" not in spec:
        spec["theme"] = {}

    if "traditional" in instruction_lower or "पारंपारिक" in instruction_lower:
        spec["theme"]["style"] = "traditional"
        spec["theme"]["primary_color"] = "#C84B31"
    elif "minimal" in instruction_lower or "साधा" in instruction_lower:
        spec["theme"]["style"] = "minimal"
        spec["theme"]["primary_color"] = "#2D4059"
    elif "premium" in instruction_lower or "रॉयल" in instruction_lower:
        spec["theme"]["style"] = "premium"
        spec["theme"]["primary_color"] = "#D4AF37"
    elif "green" in instruction_lower or "हिरवा" in instruction_lower:
        spec["theme"]["primary_color"] = "#16A34A"
    elif "blue" in instruction_lower or "निळा" in instruction_lower:
        spec["theme"]["primary_color"] = "#2563EB"

    spec["version"] = spec.get("version", 1) + 1
    return spec
