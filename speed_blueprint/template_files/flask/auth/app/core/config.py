"""Application configuration with auth settings."""
import os
from datetime import timedelta
from functools import lru_cache


class Settings:
    """Application settings."""
    APP_NAME: str = "{{project_name}}"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change-me-in-production-min-32-chars")

    # JWT Settings
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    REFRESH_TOKEN_EXPIRE_DAYS: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))

    # Security
    PASSWORD_MIN_LENGTH: int = 8
    ALLOWED_ORIGINS: list = os.getenv(
        "ALLOWED_ORIGINS", "http://localhost:3000"
    ).split(",")


@lru_cache()
def get_settings() -> Settings:
    return Settings()
