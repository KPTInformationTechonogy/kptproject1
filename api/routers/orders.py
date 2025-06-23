from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..crud import orders, products
from ..deps import get_db, user_dependency

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post("/", response_model=schemas.Order)
def create_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(user_dependency)
):
    # Verify the product exists
    db_product = products.get_product(db, product_id=order.product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Verify sufficient stock
    if db_product.quantity < order.quantity:
        raise HTTPException(status_code=400, detail="Insufficient stock")
    
    # Calculate total price
    total_price = db_product.price * order.quantity
    
    # Create order
    order_data = order.dict()
    order_data["total_price"] = total_price
    order_data["user_id"] = current_user.id
    db_order = crud.create_order(db=db, order=schemas.OrderCreate(**order_data))
    
    # Update product quantity
    db_product.quantity -= order.quantity
    db.commit()
    db.refresh(db_product)
    
    return db_order

@router.get("/", response_model=List[schemas.Order])
def read_orders(
    skip: int = 0, 
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(user_dependency)
):
    if current_user.role == "admin":
        order = orders.get_orders(db, skip=skip, limit=limit)
    else:
        order = orders.get_orders_by_user(db, user_id=current_user.id)
    return order

@router.get("/{order_id}", response_model=schemas.Order)
def read_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(user_dependency)
):
    db_order = orders.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    if db_order.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    return db_order

@router.put("/{order_id}", response_model=schemas.Order)
def update_order(
    order_id: int,
    order: schemas.OrderUpdate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(user_dependency)
):
    db_order = orders.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    if db_order.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    return orders.update_order(db=db, order_id=order_id, order=order)

@router.delete("/{order_id}", response_model=schemas.Order)
def delete_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(user_dependency)
):
    db_order = orders.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    if db_order.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    return orders.delete_order(db=db, order_id=order_id)