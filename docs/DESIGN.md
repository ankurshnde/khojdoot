# 🎨 KhojDoot Design System (`DESIGN.md`)

> **PS-29: Regional-Language No-Code Website Platform**  
> Visual & Structural Design Tokens for Indic MSME Websites.

---

## 1. Typography Hierarchy

| Role | Font Family | Size (Mobile) | Size (Desktop) | Weight | Devanagari Support |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Headline / Hero** | `Noto Sans Devanagari, sans-serif` | `2.25rem` (`36px`) | `3.0rem` (`48px`) | `700` Bold | Full Unicode |
| **Section Heading** | `Noto Sans Devanagari, sans-serif` | `1.5rem` (`24px`) | `2.0rem` (`32px`) | `600` Semi-bold | Full Unicode |
| **Body / Description** | `Noto Sans Devanagari, sans-serif` | `1.0rem` (`16px`) | `1.125rem` (`18px`) | `400` Regular | Full Unicode |
| **Pricing Badge** | `system-ui, sans-serif` | `1.25rem` (`20px`) | `1.5rem` (`24px`) | `700` Bold | Currency symbol `₹` |

---

## 2. Palette & Themes

### Theme A: **Traditional / Marathi Rasoi** (`traditional`)
* Primary: `#C84B31` (Deep Terracotta / Kesari)
* Secondary: `#2D4059` (Slate Navy)
* Background: `#FAF8F5` (Warm Cream)
* Surface / Card: `#FFFFFF`
* Text: `#1F2937` (Charcoal)

### Theme B: **Modern Fresh / Groceries & Kirana** (`minimal`)
* Primary: `#16A34A` (Fresh Green)
* Secondary: `#0F172A` (Deep Slate)
* Background: `#F8FAFC` (Cool Off-White)
* Surface / Card: `#FFFFFF`
* Text: `#0F172A`

### Theme C: **Royal / Premium Services** (`premium`)
* Primary: `#D4AF37` (Warm Gold)
* Secondary: `#1E1B4B` (Midnight Indigo)
* Background: `#0B0F19` (Dark Luxury)
* Surface / Card: `#161F30`
* Text: `#F3F4F6`

---

## 3. Touch Targets & Mobile Usability (Bharat Standard)
1. **Interactive Touch Targets**: Minimum height and width $\ge 48\text{px} \times 48\text{px}$ for all CTA buttons (Call, WhatsApp, Maps).
2. **Floating Action Bar (FAB)**: Persistent bottom bar on mobile featuring:
   - Call Now button (`tel:+91...`)
   - WhatsApp button (`https://wa.me/91...?text=...`)
3. **Contrast Ratio**: $\ge 4.5:1$ contrast against backgrounds for outdoor sunlight visibility.

---

## 4. Crawlable Asset Structure per Merchant
For every merchant `https://localhost:8000/merchant/{slug}`, the following assets are co-located:

```
generated/{slug}/
├── index.html            <- Main website + embedded JSON-LD
├── facts.json            <- High-speed attribute dictionary
├── agentfacts.json       <- AgentFacts Protocol definition
├── agent-card.json       <- A2A Agent Card metadata
├── llms.txt              <- Compact context for LLM crawlers
├── llms-full.txt         <- Full offerings and catalog context
├── robots.txt            <- Crawler allowances and sitemap path
└── sitemap.xml           <- Search engine indexing specification
```
