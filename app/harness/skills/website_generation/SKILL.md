---
name: website-generation
description: Translates validated InfoBin facts and WebsiteSpec presentation models into fast, lightweight, semantic HTML5 with Tailwind CSS styling and JSON-LD schema.
---

# Website Generation Skill

## Core Principles
1. **Lightweight & High Speed**: Websites must load instantly on 2G/3G mobile networks. Zero heavy JS framework bundles (no React, Vue, or bulky client runtimes).
2. **Deterministic Layout Blocks**:
   - **Hero Section**: Business title in Noto Sans Devanagari, tagline/services, instant Call/WhatsApp action buttons.
   - **Products / Menu**: High-contrast grid/list with clear pricing in `₹`.
   - **Location & Hours**: Operating hours badge, clear address, and Google Maps intent link.
   - **Contact Section**: One-tap `tel:` and `https://wa.me/91...` interactive CTA links.
   - **Footer**: Verified by KhojDoot badge.
3. **Structured Data Injection**: Embed Schema.org `LocalBusiness` JSON-LD `<script>` tag inside `<head>`.
4. **Devanagari Font**: Guarantee `<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;600;700&display=swap" rel="stylesheet">` and `font-family: 'Noto Sans Devanagari', sans-serif;`.
