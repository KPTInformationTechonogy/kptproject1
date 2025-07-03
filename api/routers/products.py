from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import  schemas
from ..crud import  products
from ..deps import get_db, admin_dependency

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/create", response_model=schemas.Product)
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(admin_dependency)
):
    # Verify the business belongs to the user
    db_business = products.get_business(db, business_id=product.business_id)
    if not db_business:
        raise HTTPException(status_code=404, detail="Business not found")
    if db_business.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.create_product(db=db, product=product)

@router.get("/", response_model=List[schemas.Product])
def read_products(
    skip: int = 0, 
    limit: int = 100,
    db: Session = Depends(get_db)
):
    product = products.get_products(db, skip=skip, limit=limit)
    return product

@router.get("/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = products.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.put("/{product_id}", response_model=schemas.Product)
def update_product(
    product_id: int,
    product: schemas.ProductUpdate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(admin_dependency)
):
    db_product = products.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db_business = products.get_business(db, business_id=db_product.business_id)
    if db_business.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    
    return products.update_product(db=db, product_id=product_id, product=product)

@router.delete("/{product_id}", response_model=schemas.Product)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(admin_dependency)
):
    db_product = products.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db_business = products.get_business(db, business_id=db_product.business_id)
    if db_business.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    
    return products.delete_product(db=db, product_id=product_id)