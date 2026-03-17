"""Initialize database with sample data."""
from sqlalchemy.orm import Session
from app.crud.item import create_item
from app.schemas.item import ItemCreate


def init_db(db: Session) -> None:
    """Initialize database with sample data."""
    # Create sample items
    items = [
        ItemCreate(title="Sample Item 1", description="This is a sample item", is_active=True),
        ItemCreate(title="Sample Item 2", description="Another sample item", is_active=True),
    ]

    for item in items:
        create_item(db, item)
