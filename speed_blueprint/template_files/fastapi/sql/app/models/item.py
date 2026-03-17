"""Item model."""
from sqlalchemy import Column, Integer, String, Boolean, Text
from app.models.base import Base


class Item(Base):
    """Item model."""

    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True, nullable=False)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
