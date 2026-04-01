"""Order endpoints."""
from datetime import datetime
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.crud import order as order_crud
from app.models.order import OrderStatus
from app.models.user import User
from app.schemas.order import OrderCreate, OrderResponse, OrderUpdate

router = APIRouter()


@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new order."""
    db_order = order_crud.create_order(db=db, order=order, user_id=current_user.id)
    if not db_order:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create order. Check product availability and stock."
        )
    return db_order


@router.get("/", response_model=List[OrderResponse])
def read_orders(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    customer_id: Optional[int] = Query(None),
    status: Optional[OrderStatus] = Query(None),
    start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all orders with filtering."""
    # Non-admin users can only see their own orders
    user_id = None if current_user.is_admin else current_user.id

    orders = order_crud.get_orders(
        db,
        skip=skip,
        limit=limit,
        customer_id=customer_id,
        status=status,
        user_id=user_id,
        start_date=start_date,
        end_date=end_date
    )
    return orders


@router.get("/count")
def count_orders(
    customer_id: Optional[int] = Query(None),
    status: Optional[OrderStatus] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Count orders."""
    count = order_crud.count_orders(db, customer_id=customer_id, status=status)
    return {"count": count}


@router.get("/statistics")
def get_order_statistics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get order statistics."""
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    return order_crud.get_order_statistics(db)


@router.get("/{order_id}", response_model=OrderResponse)
def read_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a specific order."""
    order = order_crud.get_order(db, order_id=order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )

    # Non-admin users can only see their own orders
    if not current_user.is_admin and order.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )

    return order


@router.put("/{order_id}", response_model=OrderResponse)
def update_order(
    order_id: int,
    order_update: OrderUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update an order."""
    order = order_crud.get_order(db, order_id=order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )

    # Non-admin users can only update their own orders
    if not current_user.is_admin and order.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )

    updated_order = order_crud.update_order(db, order_id=order_id, order_update=order_update)
    return updated_order


@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete an order."""
    order = order_crud.get_order(db, order_id=order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )

    # Non-admin users can only delete their own orders
    if not current_user.is_admin and order.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )

    deleted = order_crud.delete_order(db, order_id=order_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return None
