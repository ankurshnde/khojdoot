---
name: requirement-understanding
description: Analyzes regional Indic natural language (Marathi/Hindi/English voice notes or text) to classify intent, identify business domain, and extract key merchant attributes.
---

# Requirement Understanding Skill

## Overview
This skill guides the Agent Harness in deciphering spoken or typed input from Indian local merchants (MSMEs, kirana stores, tiffin services, tailors, eateries).

## Intent Taxonomy
1. **`NEW_BUSINESS_INFO`**:
   - Merchant is providing new facts about their establishment.
   - Example (Marathi): *"आमची सुनीता टिफिन सर्व्हिस आहे, गंगापूर रोड नाशिक. रोज घरगुती जेवणाचा डबा ८० रुपयांत मिळतो."*
2. **`EDIT_REQUEST`**:
   - Merchant wants to modify their generated website design, colors, pricing, or content.
   - Example (Marathi): *"रंग हिरवा करा आणि साधा लूक ठेवा."*
3. **`CLARIFICATION`**:
   - Merchant is responding to a missing field prompt (e.g. providing an alternate phone number or opening hours).

## Execution Directives
- **Zero Hallucination**: Do not fabricate prices, contact numbers, or certifications not explicitly stated by the merchant.
- **Dialect & Transliteration Resilience**: Support mixed Marathi-English ("Nashik madhe home delivery ahe"), Devanagari script, and Latin script transliteration.
- **Entity Identification**: Tag merchant name, locality, phone pattern, product category, and price mentions.
