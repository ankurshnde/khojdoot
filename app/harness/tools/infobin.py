"""InfoBin Tool."""
from app.db.crud import save_bin, get_bin

def tool_save_infobin(shop_id: int, bin_type: str, data: dict):
    save_bin(shop_id, bin_type, data)
