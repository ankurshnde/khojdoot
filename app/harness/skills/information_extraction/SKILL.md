---
name: information-extraction
description: Extracts structured business entities into canonical InfoBin schema with provenance tracking, consent validation, and regional numeral normalization.
---

# Information Extraction Skill
Owner: Paksha (AI & Prompt Engineering Lead) / Ankur (Architecture Lead)

## Target Schema (`InfoBin`)
The agent extracts facts into the canonical Pydantic `InfoBin` model:
- `name` (str): Trade name of the business (preserve original regional script)
- `phone` (str): Valid 10-digit Indian mobile number (`+91` or `[6-9]\d{9}`)
- `location` (str): Street address, landmark, town/city
- `services` (str): Core business offerings or specialty summary
- `hours` (str): Operating days and timing
- `menu` (List[MenuItem]): Array of `{item: str, price: float}`
- `language` (str): Regional language tag (`mr-IN`, `hi-IN`, `te-IN`, `en-IN`)

## Normalization & Prompt Rules
1. **Indic Numerals**: Convert Devanagari numerals to standard ASCII (`०` -> `0`, `१` -> `1`, `८०` -> `80`).
2. **Verbatim Script Preservation**: Preserve original script for proper nouns, shop names, and regional delicacies (e.g., "गणेश मिसळ", "साधा डबा", "स्पेशल थाळी").
3. **Zero Hallucination**: Never invent prices or contact numbers. If price is absent or unreadable, return `null`.
4. **Multimodal Ingestion**:
   - For photos, extract visible text from shop signboards, rate-cards, printed pamphlets, and menu boards.
   - Ignore background clutter or customer names on bills.
5. **Fallback Safety**: If the Gemini API is unreachable or unconfigured, fallback deterministic regex parsing handles core entities to ensure pipeline resilience.
