---
name: information-extraction
description: Extracts structured business entities into canonical InfoBin schema with provenance tracking, consent validation, and regional numeral normalization.
---

# Information Extraction Skill

## Target Schema (`InfoBin`)
The agent extracts facts into the canonical Pydantic `InfoBin` model:
- `name` (str): Trade name of the business
- `phone` (str): Valid 10-digit Indian mobile number (`+91` or `[6-9]\d{9}`)
- `location` (str): Street address, landmark, town/city
- `services` (str): Core business offerings or specialty
- `hours` (str): Operating days and timing
- `menu` (List[MenuItem]): Array of `{item: str, price: str}`

## Normalization Rules
1. **Indic Numerals**: Convert Devanagari numerals to standard ASCII (`०` -> `0`, `१` -> `1`, `८०` -> `80`).
2. **Currency Formatting**: Format prices with Rupee symbol `₹` without adding unexpected decimals.
3. **Phone Formatting**: Standardize to E.164 or canonical Indian 10-digit format (`+91 9423375197`).
4. **Provenance Tagging**: Every extracted key must record the source utterance (`raw_input`), confidence score, and timestamp.
