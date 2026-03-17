"""Item schemas."""
from pydantic import BaseModel


class ItemBase(BaseModel):
    """Base item schema."""
    title: str
    description: str | None = None
    is_active: bool = True


class ItemCreate(ItemBase):
    """Item creation schema."""
    pass


class ItemUpdate(ItemBase):
    """Item update schema."""
    pass


class Item(ItemBase):
    """Item schema."""
    id: int

    class Config:
        from_attributes = True
