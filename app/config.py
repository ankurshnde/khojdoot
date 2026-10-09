"""
Application Configuration.
Owner: Abhishek / System Architecture
"""
import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    BASE_URL: str = "http://localhost:8000"

    DATABASE_URL: str = "sqlite:///./data/khoj_doot.db"
    DATABASE_PATH: str = "./data/khoj_doot.db"

    UPLOAD_DIR: str = "./data/uploads"
    GENERATED_DIR: str = "./generated"

    GEMINI_API_KEY: str = ""
    SARVAM_API_KEY: str = ""

    CODING_MODEL_PROVIDER: str = "gemini"
    CODING_MODEL_NAME: str = "gemini-2.5-flash"

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()
