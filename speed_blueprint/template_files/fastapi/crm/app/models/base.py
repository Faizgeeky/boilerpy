"""Base model imports to register all models."""
from app.core.database import Base  # noqa: F401
from app.models.user import User  # noqa: F401
from app.models.customer import Customer  # noqa: F401
from app.models.product import Product  # noqa: F401
from app.models.order import Order, OrderItem  # noqa: F401
