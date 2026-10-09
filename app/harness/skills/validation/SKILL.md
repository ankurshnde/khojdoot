---
name: validation
description: Runs the strict 8-point deterministic website validator and InfoBin business rule compliance suite.
---

# Validation Skill

## 8-Point Website Quality Scorecard
Every generated website must pass the 8-point validation suite before reaching Checkpoint 2:
1. **Semantic HTML5 Structure**: `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`, properly closed tags.
2. **Viewport Meta Tag**: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`.
3. **UTF-8 Charset Declaration**: `<meta charset="UTF-8">` ensuring zero garbled Devanagari characters.
4. **Valid Title Tag**: Non-empty `<title>` containing business name.
5. **Schema.org JSON-LD**: Valid embedded JSON-LD containing `@type: LocalBusiness`.
6. **Actionable Contact CTAs**: Functional `tel:` or `https://wa.me/` link present.
7. **Zero Insecure External Scripts**: No untrusted third-party trackers or heavy JS dependencies.
8. **Responsive Layout Container**: Clean inline/Tailwind container styling for mobile and desktop screens.
