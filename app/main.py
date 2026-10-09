"""
FastAPI Main Application Entrypoint.
Owner: Abhishek (Backend / FastAPI Engineer)
Boundary: Application setup, middleware, routing, and lifecycle.
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.config import settings
from app.db.database import init_db
from app.routes.merchants import router as merchants_router
from app.routes.website import router as website_router
from app.routes.assets import router as assets_router
from app.routes.auth import router as auth_router

# Ensure runtime directories exist
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
os.makedirs(settings.GENERATED_DIR, exist_ok=True)

# Initialize database schema
init_db()

app = FastAPI(
    title="KhojDoot API",
    description="Regional-Language No-Code Website Creation Platform",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static mounts
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")
if os.path.exists(settings.GENERATED_DIR):
    app.mount("/static/generated", StaticFiles(directory=settings.GENERATED_DIR), name="generated")
if os.path.exists(settings.UPLOAD_DIR):
    app.mount("/static/uploads", StaticFiles(directory=settings.UPLOAD_DIR), name="uploads")


# Include Routers
app.include_router(auth_router, prefix="/api/auth", tags=["Authentication & OTP"])
app.include_router(merchants_router, prefix="/api/merchants", tags=["Merchants & Chat"])
app.include_router(website_router, prefix="/api/website", tags=["Website Engine & Editing"])
app.include_router(assets_router, tags=["Publishing & Public Assets"])



@app.get("/health", tags=["Health"])
def health_check():
    """Checkpoint 1: FastAPI Application & Health Endpoint."""
    return {
        "status": "healthy",
        "service": "KhojDoot Backend",
        "version": "2.0.0",
    }


@app.get("/api", tags=["Root"])
def api_root():
    return {
        "message": "Welcome to KhojDoot API. Check /docs for documentation.",
        "health": "/health",
    }


@app.get("/", tags=["Root"])
def root():
    import os
    from fastapi.responses import HTMLResponse
    template_path = os.path.join(os.path.dirname(__file__), "templates", "index.html")
    if os.path.exists(template_path):
        with open(template_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return {
        "message": "Welcome to KhojDoot API. Check /docs for documentation.",
        "health": "/health",
    }

