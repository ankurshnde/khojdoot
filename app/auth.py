"""
Authentication & OTP Module (User ID = Mobile Number).
Re-exports routes and helper functions.
"""
from app.routes.auth import router, normalize_mobile, DEMO_MASTER_OTP, OTP_STORE

__all__ = ["router", "normalize_mobile", "DEMO_MASTER_OTP", "OTP_STORE"]
