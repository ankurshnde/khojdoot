"""Merchant Tool."""
from app.db.crud import create_or_update_shop, get_shop_by_slug

def tool_create_merchant(sme_id: str, slug: str, name: str, phone: str = "", city: str = ""):
    return create_or_update_shop(sme_id, slug, name, phone, city)
