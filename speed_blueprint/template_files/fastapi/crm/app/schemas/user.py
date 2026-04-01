"""User schemas."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserBase(BaseModel):
    """Base user schema."""
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True
    is_admin: bool = False


class UserCreate(UserBase):
    """Schema for creating a user."""
    password: str = Field(..., min_length=8)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "user@example.com",
                "full_name": "John Doe",
                "password": "strongpassword123",
                "is_active": True,
                "is_admin": False
            }
        }
    )


class UserUpdate(BaseModel):
    """Schema for updating a user."""
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None
    is_admin: Optional[bool] = None
    password: Optional[str] = Field(None, min_length=8)


class UserResponse(UserBase):
    """Schema for user response."""
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
