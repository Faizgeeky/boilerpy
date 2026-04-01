"""Security utilities for password hashing and JWT."""
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta
from app.core.config import get_settings


def hash_password(password: str) -> str:
    """Hash a password using werkzeug."""
    return generate_password_hash(password, method='pbkdf2:sha256')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against a hash."""
    return check_password_hash(hashed_password, plain_password)


def create_tokens(user_id: str):
    """Create access and refresh tokens for a user."""
    settings = get_settings()

    access_token = create_access_token(
        identity=user_id,
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    refresh_token = create_refresh_token(
        identity=user_id,
        expires_delta=timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }
