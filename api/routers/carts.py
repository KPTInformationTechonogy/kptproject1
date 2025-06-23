from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..deps import get_db, user_dependency

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)

@router.post("/", response_model=schemas.Cart)
def add_to_cart(
    cart: schemas.CartCreate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(user_dependency)
):
    # Verify the product exists
    db_product = crud.get_product(db, product_id=cart.product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Check if item already in cart
    existing_item = db.query(crud.Cart).filter(
        crud.Cart.user_id == current_user.id,
        crud.Cart.product_id == cart.product_id,
        crud.Cart.is_active == True
    ).first()
    
    if existing_item:
        # Update quantity if item exists
        existing_item.quantity += cart.quantity
        db.commit()
        db.refresh(existing_item)
        return existing_item
    else:
        # Add new item to cart
        cart_data = cart.dict()
        cart_data["user_id"] = current_user.id
        return crud.create_cart_item(db=db, cart=schemas.CartCreate(**cart_data))

@router.get("/", response_model=List[schemas.Cart])
def get_cart(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(user_dependency)
):
    return crud.get_cart_items(db, user_id=current_user.id)

@router.put("/{cart_id}", response_model=schemas.Cart)
def update_cart_item(
    cart_id: int,
    cart: schemas.CartUpdate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(user_dependency)
):
    db_cart = crud.get_cart_item(db, cart_id=cart_id)
    if db_cart is None:
        raise HTTPException(status_code=404, detail="Cart item not found")
    if db_cart.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.update_cart_item(db=db, cart_id=cart_id, cart=cart)

@router.delete("/{cart_id}", response_model=schemas.Cart)
def remove_from_cart(
    cart_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(user_dependency)
):
    db_cart = crud.get_cart_item(db, cart_id=cart_id)
    if db_cart is None:
        raise HTTPException(status_code=404, detail="Cart item not found")
    if db_cart.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.delete_cart_item(db=db, cart_id=cart_id)

@router.post("/checkout", response_model=schemas.Order)
def checkout_cart(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(user_dependency)
):
    cart_items = crud.get_cart_items(db, user_id=current_user.id)
    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")
    
    # Create orders for each cart item
    orders = []
    for item in cart_items:
        order_data = {
            "user_id": current_user.id,
            "product_id": item.product_id,
            "quantity": item.quantity,
            "total_price": item.product.price * item.quantity
        }
        db_order = crud.create_order(db=db, order=schemas.OrderCreate(**order_data))
        orders.append(db_order)
    
    # Clear the cart
    crud.clear_user_cart(db, user_id=current_user.id)
    
    return orders[0]  # Return the first order for simplicity