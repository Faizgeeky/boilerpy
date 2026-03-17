"""Application configuration."""
from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    PROJECT_NAME: str = "{{project_name}}"
    API_V1_STR: str = "/api/v1"
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]

    # Database
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/{{project_name_snake}}"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
