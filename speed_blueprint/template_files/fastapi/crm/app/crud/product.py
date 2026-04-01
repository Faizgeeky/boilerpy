"""Product CRUD operations."""
from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


def get_product(db: Session, product_id: int) -> Optional[Product]:
    """Get a product by ID."""
    return db.query(Product).filter(Product.id == product_id).first()


def get_product_by_sku(db: Session, sku: str) -> Optional[Product]:
    """Get a product by SKU."""
    return db.query(Product).filter(Product.sku == sku).first()


def get_products(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    is_active: Optional[bool] = None,
    search: Optional[str] = None
) -> List[Product]:
    """Get all products with optional filtering."""
    query = db.query(Product)

    if is_active is not None:
        query = query.filter(Product.is_active == is_active)

    if search:
        search_filter = f"%{search}%"
        query = query.filter(
            (Product.name.ilike(search_filter)) |
            (Product.sku.ilike(search_filter)) |
            (Product.description.ilike(search_filter))
        )

    return query.offset(skip).limit(limit).all()


def create_product(db: Session, product: ProductCreate) -> Product:
    """Create a new product."""
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product_id: int, product_update: ProductUpdate) -> Optional[Product]:
    """Update a product."""
    db_product = get_product(db, product_id)
    if not db_product:
        return None

    update_data = product_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_product, field, value)

    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int) -> bool:
    """Delete a product."""
    db_product = get_product(db, product_id)
    if not db_product:
        return False

    db.delete(db_product)
    db.commit()
    return True


def update_stock(db: Session, product_id: int, quantity_change: int) -> Optional[Product]:
    """Update product stock."""
    db_product = get_product(db, product_id)
    if not db_product:
        return None

    db_product.stock += quantity_change
    db.commit()
    db.refresh(db_product)
    return db_product


def count_products(db: Session, is_active: Optional[bool] = None) -> int:
    """Count total products."""
    query = db.query(Product)
    if is_active is not None:
        query = query.filter(Product.is_active == is_active)
    return query.count()
