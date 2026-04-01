"""Customer schemas."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class CustomerBase(BaseModel):
    """Base customer schema."""
    name: str = Field(..., min_length=1, max_length=200)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, max_length=50)
    company: Optional[str] = Field(None, max_length=200)
    address: Optional[str] = None
    notes: Optional[str] = None


class CustomerCreate(CustomerBase):
    """Schema for creating a customer."""

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Acme Corporation",
                "email": "contact@acme.com",
                "phone": "+1-555-0123",
                "company": "Acme Corp",
                "address": "123 Main St, City, State 12345",
                "notes": "VIP customer"
            }
        }
    )


class CustomerUpdate(BaseModel):
    """Schema for updating a customer."""
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, max_length=50)
    company: Optional[str] = Field(None, max_length=200)
    address: Optional[str] = None
    notes: Optional[str] = None


class CustomerResponse(CustomerBase):
    """Schema for customer response."""
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
