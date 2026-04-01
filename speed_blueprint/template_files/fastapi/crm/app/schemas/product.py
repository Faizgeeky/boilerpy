"""Product schemas."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class ProductBase(BaseModel):
    """Base product schema."""
    name: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    sku: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    is_active: bool = True


class ProductCreate(ProductBase):
    """Schema for creating a product."""

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Premium Widget",
                "description": "High-quality widget with advanced features",
                "sku": "WIDGET-001",
                "price": 99.99,
                "stock": 100,
                "is_active": True
            }
        }
    )


class ProductUpdate(BaseModel):
    """Schema for updating a product."""
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    sku: Optional[str] = Field(None, min_length=1, max_length=100)
    price: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    is_active: Optional[bool] = None


class ProductResponse(ProductBase):
    """Schema for product response."""
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
