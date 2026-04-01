"""Item schemas for request/response."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class ItemCreate(BaseModel):
    """Schema for creating an item."""

    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)
    is_active: bool = Field(default=True)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "New Item",
                "description": "A brand new item",
                "price": 19.99,
                "quantity": 50,
                "is_active": True
            }
        }
    )


class ItemUpdate(BaseModel):
    """Schema for updating an item."""

    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: Optional[float] = Field(None, gt=0)
    quantity: Optional[int] = Field(None, ge=0)
    is_active: Optional[bool] = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Updated Item",
                "price": 24.99,
                "quantity": 75
            }
        }
    )


class ItemResponse(BaseModel):
    """Schema for item response."""

    id: str = Field(..., alias="_id")
    name: str
    description: Optional[str] = None
    price: float
    quantity: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )
