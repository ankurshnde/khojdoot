"""Products & Menu Catalog Component.
Adheres to docs/DESIGN.md:
- Pricing Badge: system-ui, sans-serif, 1.25rem - 1.5rem, weight 700 bold, Currency symbol ₹
- Card surfaces with responsive touch targets and clean contrast
"""
from typing import List, Dict, Any, Optional


def render_products(
    items: List[Dict[str, Any]],
    theme: Optional[Dict[str, Any]] = None,
    language: str = "mr-IN",
    title: Optional[str] = None,
) -> str:
    theme = theme or {}
    primary = theme.get("primary", "#C84B31")
    surface = theme.get("surface", "#FFFFFF")
    text_color = theme.get("text", "#1F2937")

    if not title:
        if "te" in language:
            title = "మెనూ & సేవల జాబితా / Menu & Pricing"
        elif "hi" in language:
            title = "मेन्यू एवं मूल्य सूची / Menu & Pricing"
        elif "en" in language:
            title = "Offerings, Catalog & Pricing"
        else:
            title = "मेन्यू आणि दर / Menu & Pricing"

    if not items:
        return ""

    items_html = ""
    for item in items:
        name = item.get("item", "")
        price = item.get("price", "")
        price_str = f"₹{price}" if price else "दर चौकशीवर / On Request"

        items_html += f"""
        <div class="product-item-card" style="
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 16px 20px;
            background: {surface};
            border: 1px solid #E5E7EB;
            border-radius: 10px;
            margin-bottom: 12px;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
            transition: transform 0.15s ease;
        ">
            <div style="flex: 1; padding-right: 12px;">
                <span style="font-size: 1.125rem; font-weight: 600; color: {text_color}; line-height: 1.35; display: block;">
                    {name}
                </span>
            </div>
            <div>
                <span class="price-badge" style="
                    font-family: system-ui, -apple-system, sans-serif;
                    font-size: 1.25rem;
                    font-weight: 700;
                    color: {primary};
                    background: rgba(0, 0, 0, 0.03);
                    padding: 6px 14px;
                    border-radius: 8px;
                    display: inline-block;
                    white-space: nowrap;
                    border: 1px solid rgba(0, 0, 0, 0.06);
                ">
                    {price_str}
                </span>
            </div>
        </div>
        """

    return f"""
    <section id="products" class="products-section" style="padding: 48px 20px; max-width: 820px; margin: 0 auto;">
        <h2 style="
            font-size: clamp(1.6rem, 4vw, 2.0rem);
            font-weight: 700;
            text-align: center;
            margin-bottom: 28px;
            color: {text_color};
            letter-spacing: -0.02em;
        ">
            {title}
        </h2>
        <div class="products-list">
            {items_html}
        </div>
    </section>
    """
