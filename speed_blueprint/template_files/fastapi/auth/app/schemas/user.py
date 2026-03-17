"""User schemas."""
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """Base user schema."""
    username: str
    email: EmailStr


class UserCreate(UserBase):
    """User creation schema."""
    password: str


class User(UserBase):
    """User schema."""
    pass


class UserInDB(User):
    """User in database schema."""
    hashed_password: str
