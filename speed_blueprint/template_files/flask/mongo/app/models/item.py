"""Item model for MongoDB."""
from datetime import datetime
from typing import Optional, Dict, Any
from bson import ObjectId


class Item:
    """Item model representing a document in MongoDB."""

    collection_name = "items"

    def __init__(
        self,
        title: str,
        description: Optional[str] = None,
        price: float = 0.0,
        quantity: int = 0,
        category: Optional[str] = None,
        _id: Optional[ObjectId] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        """Initialize Item instance."""
        self._id = _id or ObjectId()
        self.title = title
        self.description = description
        self.price = price
        self.quantity = quantity
        self.category = category
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def to_dict(self) -> Dict[str, Any]:
        """Convert item to dictionary."""
        return {
            "id": str(self._id),
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    def to_mongo(self) -> Dict[str, Any]:
        """Convert item to MongoDB document format."""
        return {
            "_id": self._id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_mongo(cls, doc: Dict[str, Any]) -> "Item":
        """Create Item instance from MongoDB document."""
        return cls(
            _id=doc.get("_id"),
            title=doc.get("title"),
            description=doc.get("description"),
            price=doc.get("price", 0.0),
            quantity=doc.get("quantity", 0),
            category=doc.get("category"),
            created_at=doc.get("created_at"),
            updated_at=doc.get("updated_at"),
        )
