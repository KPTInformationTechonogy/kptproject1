from ..models import Businesses
from ..schemas import BusinessCreate, BusinessUpdate
from sqlalchemy.orm import Session

def get_business(db: Session, business_id: int):
    return db.query(Businesses).filter(Businesses.id == business_id, Businesses.is_active == True).first()

def get_businesses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Businesses).filter(Businesses.is_active == True).offset(skip).limit(limit).all()

def get_businesses_by_user(db: Session, user_id: int):
    return db.query(Businesses).filter(Businesses.user_id == user_id, Businesses.is_active == True).all()

def create_business(db: Session, business: BusinessCreate, user_id: int):
    db_business = Businesses(
        user_id=user_id,
        name=business.name,
        description=business.description,
        email=business.email,
        phone_number=business.phone_number
    )
    db.add(db_business)
    db.commit()
    db.refresh(db_business)
    return db_business

def update_business(db: Session, business_id: int, business: BusinessUpdate):
    db_business = get_business(db, business_id)
    if not db_business:
        return None
    
    update_data = business.dict(exclude_unset=True)
    for field in update_data:
        setattr(db_business, field, update_data[field])
    
    db.commit()
    db.refresh(db_business)
    return db_business

def delete_business(db: Session, business_id: int):
    db_business = get_business(db, business_id)
    if not db_business:
        return None
    
    db_business.is_active = False
    db_business.deleted_at = func.now()
    db.commit()
    return db_business