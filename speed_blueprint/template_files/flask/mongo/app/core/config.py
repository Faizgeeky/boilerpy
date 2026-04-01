"""Application configuration."""
import os
from functools import lru_cache
from typing import List


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
    ALLOWED_ORIGINS: List[str] = os.getenv("ALLOWED_ORIGINS", "*").split(",")

    # MongoDB Configuration
    MONGO_URI: str = os.getenv(
        "MONGO_URI",
        "mongodb://admin:admin@localhost:27017/{{project_name}}?authSource=admin"
    )

    # MongoDB Database Name
    MONGO_DBNAME: str = os.getenv("MONGO_DBNAME", "{{project_name}}")


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
