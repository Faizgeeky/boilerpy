"""Item model for MongoDB."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class ItemModel(BaseModel):
    """Item document model."""

    id: Optional[str] = Field(None, alias="_id")
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "name": "Example Item",
                "description": "This is an example item",
                "price": 29.99,
                "quantity": 100,
                "is_active": True
            }
        }
    )
