"""Order CRUD operations."""
from datetime import datetime
from typing import List, Optional
from sqlalchemy.orm import Session, joinedload

from app.models.order import Order, OrderItem, OrderStatus
from app.models.product import Product
from app.schemas.order import OrderCreate, OrderUpdate


def get_order(db: Session, order_id: int) -> Optional[Order]:
    """Get an order by ID with items."""
    return db.query(Order).options(joinedload(Order.items)).filter(Order.id == order_id).first()


def get_orders(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    customer_id: Optional[int] = None,
    status: Optional[OrderStatus] = None,
    user_id: Optional[int] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None
) -> List[Order]:
    """Get orders with filtering."""
    query = db.query(Order).options(joinedload(Order.items))

    if customer_id:
        query = query.filter(Order.customer_id == customer_id)

    if status:
        query = query.filter(Order.status == status)

    if user_id:
        query = query.filter(Order.user_id == user_id)

    if start_date:
        query = query.filter(Order.created_at >= start_date)

    if end_date:
        query = query.filter(Order.created_at <= end_date)

    return query.order_by(Order.created_at.desc()).offset(skip).limit(limit).all()


def create_order(db: Session, order: OrderCreate, user_id: int) -> Optional[Order]:
    """Create a new order with items."""
    # Calculate total and create order items
    total_amount = 0.0
    order_items = []

    for item in order.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            return None

        if product.stock < item.quantity:
            return None  # Insufficient stock

        subtotal = product.price * item.quantity
        total_amount += subtotal

        order_item = OrderItem(
            product_id=item.product_id,
            quantity=item.quantity,
            unit_price=product.price,
            subtotal=subtotal
        )
        order_items.append(order_item)

        # Update product stock
        product.stock -= item.quantity

    # Create order
    db_order = Order(
        customer_id=order.customer_id,
        user_id=user_id,
        total_amount=total_amount,
        notes=order.notes,
        status=OrderStatus.PENDING
    )
    db.add(db_order)
    db.flush()  # Get the order ID

    # Add items to order
    for order_item in order_items:
        order_item.order_id = db_order.id
        db.add(order_item)

    db.commit()
    db.refresh(db_order)
    return db_order


def update_order(db: Session, order_id: int, order_update: OrderUpdate) -> Optional[Order]:
    """Update an order."""
    db_order = get_order(db, order_id)
    if not db_order:
        return None

    update_data = order_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_order, field, value)

    db.commit()
    db.refresh(db_order)
    return db_order


def delete_order(db: Session, order_id: int) -> bool:
    """Delete an order."""
    db_order = get_order(db, order_id)
    if not db_order:
        return False

    # Return stock to products
    for item in db_order.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if product:
            product.stock += item.quantity

    db.delete(db_order)
    db.commit()
    return True


def count_orders(
    db: Session,
    customer_id: Optional[int] = None,
    status: Optional[OrderStatus] = None
) -> int:
    """Count orders."""
    query = db.query(Order)

    if customer_id:
        query = query.filter(Order.customer_id == customer_id)

    if status:
        query = query.filter(Order.status == status)

    return query.count()


def get_order_statistics(db: Session) -> dict:
    """Get order statistics."""
    from sqlalchemy import func

    total_orders = db.query(Order).count()
    total_revenue = db.query(func.sum(Order.total_amount)).scalar() or 0

    status_counts = {}
    for status in OrderStatus:
        count = db.query(Order).filter(Order.status == status).count()
        status_counts[status.value] = count

    return {
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "by_status": status_counts
    }
