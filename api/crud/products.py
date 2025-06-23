from ..models import Products
from sqlalchemy.orm import Session
from ..schemas import ProductCreate, ProductUpdate

def get_product(db: Session, product_id: int):
    return db.query(Products).filter(Products.id == product_id, Products.is_active == True).first()

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Products).filter(Products.is_active == True).offset(skip).limit(limit).all()

def get_products_by_business(db: Session, business_id: int):
    return db.query(Products).filter(Products.business_id == business_id, Products.is_active == True).all()

def create_product(db: Session, product: ProductCreate):
    db_product = Products(
        business_id=product.business_id,
        name=product.name,
        size=product.size,
        description=product.description,
        category=product.category,
        quantity=product.quantity,
        price=product.price,
        image_url=product.image_url
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    
    update_data = product.dict(exclude_unset=True)
    for field in update_data:
        setattr(db_product, field, update_data[field])
    
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    
    db_product.is_active = False
    db_product.deleted_at = func.now()
    db.commit()
    return db_product