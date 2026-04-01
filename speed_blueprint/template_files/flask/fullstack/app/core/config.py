"""Application configuration."""
import os
from functools import lru_cache
from datetime import timedelta


class Settings:
    """Application settings."""

    # Basic Configuration
    PROJECT_NAME: str = "{{project_name}}"
    VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    # Server Configuration
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "5000"))

    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    SESSION_COOKIE_SECURE: bool = not DEBUG  # Only send cookie over HTTPS in production
    SESSION_COOKIE_HTTPONLY: bool = True
    SESSION_COOKIE_SAMESITE: str = 'Lax'
    PERMANENT_SESSION_LIFETIME: timedelta = timedelta(days=7)

    # WTForms Configuration
    WTF_CSRF_ENABLED: bool = True
    WTF_CSRF_TIME_LIMIT: int = 3600  # 1 hour


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
