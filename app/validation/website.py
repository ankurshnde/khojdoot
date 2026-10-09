"""
Website Validation Suite (Checkpoint 7 & Revalidation).
Owner: Sakshi (QA / Validation)
Checks: Structural, Content, Technical, Mobile
"""
from typing import Dict, Any, List


def validate_website_html(html: str) -> Dict[str, Any]:
    checks: List[Dict[str, Any]] = []

    # Structural checks
    checks.append({"name": "has_doctype_and_html", "passed": "<!DOCTYPE html>" in html and "<html" in html})
    checks.append({"name": "has_head_and_body", "passed": "<head>" in html and "<body>" in html})

    # Content checks
    checks.append({"name": "has_title_tag", "passed": "<title>" in html and "</title>" in html})
    checks.append({"name": "has_hero_section", "passed": 'class="hero"' in html or 'id="hero"' in html})
    checks.append({"name": "has_contact_info", "passed": "tel:" in html or "wa.me" in html or "contact" in html.lower()})

    # Technical checks
    checks.append({"name": "has_json_ld", "passed": "application/ld+json" in html})
    checks.append({"name": "has_meta_charset", "passed": 'charset="UTF-8"' in html or "charset='UTF-8'" in html or "utf-8" in html.lower()})

    # Mobile check
    checks.append({"name": "has_mobile_viewport", "passed": 'name="viewport"' in html})

    passed_count = sum(1 for c in checks if c["passed"])
    total_count = len(checks)

    return {
        "score": passed_count / total_count,
        "summary": f"{passed_count}/{total_count} checks passed",
        "passed": passed_count == total_count,
        "checks": checks,
    }
