"""Customer CRUD operations."""
from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerUpdate


def get_customer(db: Session, customer_id: int) -> Optional[Customer]:
    """Get a customer by ID."""
    return db.query(Customer).filter(Customer.id == customer_id).first()


def get_customer_by_email(db: Session, email: str) -> Optional[Customer]:
    """Get a customer by email."""
    return db.query(Customer).filter(Customer.email == email).first()


def get_customers(db: Session, skip: int = 0, limit: int = 100, search: Optional[str] = None) -> List[Customer]:
    """Get all customers with optional search."""
    query = db.query(Customer)

    if search:
        search_filter = f"%{search}%"
        query = query.filter(
            (Customer.name.ilike(search_filter)) |
            (Customer.email.ilike(search_filter)) |
            (Customer.company.ilike(search_filter))
        )

    return query.offset(skip).limit(limit).all()


def create_customer(db: Session, customer: CustomerCreate) -> Customer:
    """Create a new customer."""
    db_customer = Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def update_customer(db: Session, customer_id: int, customer_update: CustomerUpdate) -> Optional[Customer]:
    """Update a customer."""
    db_customer = get_customer(db, customer_id)
    if not db_customer:
        return None

    update_data = customer_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_customer, field, value)

    db.commit()
    db.refresh(db_customer)
    return db_customer


def delete_customer(db: Session, customer_id: int) -> bool:
    """Delete a customer."""
    db_customer = get_customer(db, customer_id)
    if not db_customer:
        return False

    db.delete(db_customer)
    db.commit()
    return True


def count_customers(db: Session) -> int:
    """Count total customers."""
    return db.query(Customer).count()
