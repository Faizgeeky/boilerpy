"""Customer endpoints."""
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.crud import customer as customer_crud
from app.models.user import User
from app.schemas.customer import CustomerCreate, CustomerResponse, CustomerUpdate

router = APIRouter()


@router.post("/", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED)
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new customer."""
    if customer.email:
        db_customer = customer_crud.get_customer_by_email(db, email=customer.email)
        if db_customer:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Customer with this email already exists"
            )
    return customer_crud.create_customer(db=db, customer=customer)


@router.get("/", response_model=List[CustomerResponse])
def read_customers(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    search: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all customers with optional search."""
    customers = customer_crud.get_customers(db, skip=skip, limit=limit, search=search)
    return customers


@router.get("/count")
def count_customers(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Count total customers."""
    count = customer_crud.count_customers(db)
    return {"count": count}


@router.get("/{customer_id}", response_model=CustomerResponse)
def read_customer(
    customer_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a specific customer."""
    customer = customer_crud.get_customer(db, customer_id=customer_id)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    return customer


@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer(
    customer_id: int,
    customer_update: CustomerUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update a customer."""
    customer = customer_crud.update_customer(db, customer_id=customer_id, customer_update=customer_update)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    return customer


@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a customer."""
    deleted = customer_crud.delete_customer(db, customer_id=customer_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    return None
