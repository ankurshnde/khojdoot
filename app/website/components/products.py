"""Products & Menu Catalog Component."""
from typing import List, Dict, Any

def render_products(items: List[Dict[str, Any]], title: str = "मेन्यू आणि दर / Menu & Pricing") -> str:
    items_html = ""
    for item in items:
        name = item.get("item", "")
        price = item.get("price", "")
        price_str = f"₹{price}" if price else ""
        items_html += f"""
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 16px 20px; border-bottom: 1px solid #eee; background: #fff; border-radius: 8px; margin-bottom: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
            <span style="font-size: 1.1rem; font-weight: 600; color: #222;">{name}</span>
            <span style="font-size: 1.15rem; font-weight: 700; color: #E05A47;">{price_str}</span>
        </div>
        """
    return f"""
    <section id="products" class="products" style="padding: 50px 20px; max-width: 800px; margin: 0 auto;">
        <h2 style="font-size: 2rem; text-align: center; margin-bottom: 30px; color: #111;">{title}</h2>
        <div>{items_html}</div>
    </section>
    """
