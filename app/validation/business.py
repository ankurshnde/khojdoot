"""
Business Data Validation Engine (InfoBin).
Owner: Sakshi / Paksha
"""
from typing import Dict, Any, List
from app.schemas.infobin import InfoBin


def validate_infobin(infobin: InfoBin) -> Dict[str, Any]:
    checks = []

    # Check 1: Name presence
    name_ok = bool(infobin.name and len(infobin.name.strip()) >= 2)
    checks.append({"check": "business_name_present", "passed": name_ok})

    # Check 2: Phone presence
    phone_ok = bool(infobin.phone and len(infobin.phone.strip()) >= 8)
    checks.append({"check": "phone_valid", "passed": phone_ok})

    # Check 3: Location presence
    loc_ok = bool(infobin.location and len(infobin.location.strip()) >= 3)
    checks.append({"check": "location_present", "passed": loc_ok})

    # Check 4: Menu items / services
    menu_ok = len(infobin.menu) > 0 or bool(infobin.services)
    checks.append({"check": "offerings_or_menu_present", "passed": menu_ok})

    passed_count = sum(1 for c in checks if c["passed"])
    total_count = len(checks)

    return {
        "valid": passed_count == total_count,
        "score": passed_count / total_count,
        "summary": f"{passed_count}/{total_count} checks passed",
        "checks": checks,
    }
