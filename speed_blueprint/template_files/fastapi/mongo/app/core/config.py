"""Application configuration."""
from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    PROJECT_NAME: str = "{{project_name}}"
    API_V1_STR: str = "/api/v1"
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]

    # MongoDB settings
    MONGODB_URL: str = "mongodb://localhost:27017"
    MONGODB_DB_NAME: str = "{{project_name}}_db"

    # Collection names
    ITEMS_COLLECTION: str = "items"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
