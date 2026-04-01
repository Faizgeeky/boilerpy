"""Item schemas for request/response validation."""
from typing import Optional
from dataclasses import dataclass


@dataclass
class ItemCreate:
    """Schema for creating a new item."""
    title: str
    description: Optional[str] = None
    price: float = 0.0
    quantity: int = 0
    category: Optional[str] = None

    def validate(self) -> tuple[bool, Optional[str]]:
        """Validate item creation data."""
        if not self.title or len(self.title.strip()) == 0:
            return False, "Title is required"

        if len(self.title) > 200:
            return False, "Title must be less than 200 characters"

        if self.price < 0:
            return False, "Price must be non-negative"

        if self.quantity < 0:
            return False, "Quantity must be non-negative"

        if self.description and len(self.description) > 1000:
            return False, "Description must be less than 1000 characters"

        if self.category and len(self.category) > 100:
            return False, "Category must be less than 100 characters"

        return True, None


@dataclass
class ItemUpdate:
    """Schema for updating an item."""
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    category: Optional[str] = None

    def validate(self) -> tuple[bool, Optional[str]]:
        """Validate item update data."""
        if self.title is not None:
            if len(self.title.strip()) == 0:
                return False, "Title cannot be empty"
            if len(self.title) > 200:
                return False, "Title must be less than 200 characters"

        if self.price is not None and self.price < 0:
            return False, "Price must be non-negative"

        if self.quantity is not None and self.quantity < 0:
            return False, "Quantity must be non-negative"

        if self.description is not None and len(self.description) > 1000:
            return False, "Description must be less than 1000 characters"

        if self.category is not None and len(self.category) > 100:
            return False, "Category must be less than 100 characters"

        return True, None
