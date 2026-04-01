"""Order schemas."""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict

from app.models.order import OrderStatus


class OrderItemBase(BaseModel):
    """Base order item schema."""
    product_id: int
    quantity: int = Field(..., gt=0)


class OrderItemCreate(OrderItemBase):
    """Schema for creating an order item."""
    pass


class OrderItemResponse(OrderItemBase):
    """Schema for order item response."""
    id: int
    unit_price: float
    subtotal: float

    model_config = ConfigDict(from_attributes=True)


class OrderBase(BaseModel):
    """Base order schema."""
    customer_id: int
    notes: Optional[str] = None


class OrderCreate(OrderBase):
    """Schema for creating an order."""
    items: List[OrderItemCreate] = Field(..., min_length=1)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "customer_id": 1,
                "notes": "Urgent delivery requested",
                "items": [
                    {"product_id": 1, "quantity": 2},
                    {"product_id": 2, "quantity": 1}
                ]
            }
        }
    )


class OrderUpdate(BaseModel):
    """Schema for updating an order."""
    status: Optional[OrderStatus] = None
    notes: Optional[str] = None


class OrderResponse(OrderBase):
    """Schema for order response."""
    id: int
    user_id: int
    status: OrderStatus
    total_amount: float
    items: List[OrderItemResponse]
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
