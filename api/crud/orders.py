from ..models import Orders
from ..schemas import OrderCreate, OrderUpdate
from sqlalchemy.orm import Session

def get_order(db: Session, order_id: int):
    return db.query(Orders).filter(Orders.id == order_id, Orders.is_active == True).first()

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Orders).filter(Orders.is_active == True).offset(skip).limit(limit).all()

def get_orders_by_user(db: Session, user_id: int):
    return db.query(Orders).filter(Orders.user_id == user_id, Orders.is_active == True).all()

def create_order(db: Session, order: OrderCreate):
    db_order = Orders(
        user_id=order.user_id,
        product_id=order.product_id,
        quantity=order.quantity,
        total_price=order.total_price
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def update_order(db: Session, order_id: int, order: OrderUpdate):
    db_order = get_order(db, order_id)
    if not db_order:
        return None
    
    update_data = order.dict(exclude_unset=True)
    for field in update_data:
        setattr(db_order, field, update_data[field])
    
    db.commit()
    db.refresh(db_order)
    return db_order

def delete_order(db: Session, order_id: int):
    db_order = get_order(db, order_id)
    if not db_order:
        return None
    
    db_order.is_active = False
    db_order.deleted_at = func.now()
    db.commit()
    return db_order