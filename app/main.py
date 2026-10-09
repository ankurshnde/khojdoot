
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.projects import router as projects_router

from app.routes.generate import router as generate_router

app = FastAPI(
    title="KhojDoot API",
    description="Regional-language no-code website builder",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict this before production
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(generate_router)
app.include_router(projects_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to KhojDoot API!",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
