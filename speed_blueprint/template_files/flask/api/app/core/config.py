"""Application configuration."""
import os
from functools import lru_cache
from typing import List


class Settings:
    """Application settings."""

    # App Config
    APP_NAME: str = "{{project_name}}"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")

    # CORS
    ALLOWED_ORIGINS: List[str] = os.getenv(
        "ALLOWED_ORIGINS",
        "http://localhost:3000,http://localhost:8000"
    ).split(",")

    # API Config
    API_V1_PREFIX: str = "/api/v1"

    # Security Headers
    SECURITY_HEADERS = {
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",
        "X-XSS-Protection": "1; mode=block",
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains"
    }


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
