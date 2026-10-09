"""
WebsiteSpec Natural Language Patcher (Checkpoint 2).
Owner: Ankur / Gayatri
Applies user conversational edits into WebsiteSpec changes.
"""
from typing import Dict, Any


def patch_website_spec(spec: Dict[str, Any], edit_instruction: str) -> Dict[str, Any]:
    instruction_lower = edit_instruction.lower()

    # Style / Theme edits
    if "traditional" in instruction_lower or "पारंपारिक" in instruction_lower:
        spec["theme"]["style"] = "traditional"
        spec["theme"]["primary_color"] = "#C84B31"
    elif "minimal" in instruction_lower or "साधा" in instruction_lower:
        spec["theme"]["style"] = "minimal"
        spec["theme"]["primary_color"] = "#2D4059"
    elif "premium" in instruction_lower:
        spec["theme"]["style"] = "premium"
        spec["theme"]["primary_color"] = "#D4AF37"

    spec["version"] = spec.get("version", 1) + 1
    return spec
