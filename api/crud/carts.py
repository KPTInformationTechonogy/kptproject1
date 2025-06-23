from ..models import Cart
from ..schemas import CartCreate, CartUpdate
from sqlalchemy.orm import Session

def get_cart_item(db: Session, cart_id: int):
    return db.query(Cart).filter(Cart.id == cart_id, Cart.is_active == True).first()

def get_cart_items(db: Session, user_id: int):
    return db.query(Cart).filter(Cart.user_id == user_id, Cart.is_active == True).all()

def create_cart_item(db: Session, cart: CartCreate):
    db_cart = Cart(
        user_id=cart.user_id,
        product_id=cart.product_id,
        quantity=cart.quantity
    )
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart

def update_cart_item(db: Session, cart_id: int, cart: CartUpdate):
    db_cart = get_cart_item(db, cart_id)
    if not db_cart:
        return None
    
    update_data = cart.dict(exclude_unset=True)
    for field in update_data:
        setattr(db_cart, field, update_data[field])
    
    db.commit()
    db.refresh(db_cart)
    return db_cart

def delete_cart_item(db: Session, cart_id: int):
    db_cart = get_cart_item(db, cart_id)
    if not db_cart:
        return None
    
    db_cart.is_active = False
    db_cart.deleted_at = func.now()
    db.commit()
    return db_cart

def clear_user_cart(db: Session, user_id: int):
    cart_items = get_cart_items(db, user_id)
    for item in cart_items:
        item.is_active = False
        item.deleted_at = func.now()
    db.commit()
    return {"message": "Cart cleared successfully"}