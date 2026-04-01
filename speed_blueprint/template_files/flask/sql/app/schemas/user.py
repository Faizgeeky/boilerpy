"""User schemas for request/response validation."""
from typing import Optional
from dataclasses import dataclass
import re


def validate_email(email: str) -> bool:
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_username(username: str) -> bool:
    """Validate username format (alphanumeric and underscore only)."""
    pattern = r'^[a-zA-Z0-9_]{3,50}$'
    return bool(re.match(pattern, username))


@dataclass
class UserCreate:
    """Schema for creating a new user."""
    email: str
    username: str
    password: str
    full_name: Optional[str] = None

    def validate(self) -> tuple[bool, Optional[str]]:
        """Validate user creation data."""
        if not self.email or not validate_email(self.email):
            return False, "Invalid email format"

        if not self.username or not validate_username(self.username):
            return False, "Username must be 3-50 characters, alphanumeric and underscore only"

        if not self.password or len(self.password) < 8:
            return False, "Password must be at least 8 characters"

        return True, None


@dataclass
class UserUpdate:
    """Schema for updating a user."""
    email: Optional[str] = None
    username: Optional[str] = None
    full_name: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None

    def validate(self) -> tuple[bool, Optional[str]]:
        """Validate user update data."""
        if self.email is not None and not validate_email(self.email):
            return False, "Invalid email format"

        if self.username is not None and not validate_username(self.username):
            return False, "Username must be 3-50 characters, alphanumeric and underscore only"

        if self.password is not None and len(self.password) < 8:
            return False, "Password must be at least 8 characters"

        return True, None


@dataclass
class UserInDB:
    """Schema for user in database."""
    id: int
    email: str
    username: str
    full_name: Optional[str]
    is_active: bool
    is_superuser: bool
    created_at: str
    updated_at: str
