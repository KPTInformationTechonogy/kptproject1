from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..deps import get_db, user_dependency, admin_dependency

router = APIRouter(
    prefix="/businesses",
    tags=["Businesses"]
)

@router.post("/", response_model=schemas.Business)
def create_business(
    business: schemas.BusinessCreate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(user_dependency)
):
    return crud.create_business(db=db, business=business, user_id=current_user.id)

@router.get("/", response_model=List[schemas.Business])
def read_businesses(
    skip: int = 0, 
    limit: int = 100,
    db: Session = Depends(get_db)
):
    businesses = crud.get_businesses(db, skip=skip, limit=limit)
    return businesses

@router.get("/{business_id}", response_model=schemas.Business)
def read_business(business_id: int, db: Session = Depends(get_db)):
    db_business = crud.get_business(db, business_id=business_id)
    if db_business is None:
        raise HTTPException(status_code=404, detail="Business not found")
    return db_business

@router.put("/{business_id}", response_model=schemas.Business)
def update_business(
    business_id: int,
    business: schemas.BusinessUpdate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(user_dependency)
):
    db_business = crud.get_business(db, business_id=business_id)
    if db_business is None:
        raise HTTPException(status_code=404, detail="Business not found")
    if db_business.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.update_business(db=db, business_id=business_id, business=business)

@router.delete("/{business_id}", response_model=schemas.Business)
def delete_business(
    business_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(user_dependency)
):
    db_business = crud.get_business(db, business_id=business_id)
    if db_business is None:
        raise HTTPException(status_code=404, detail="Business not found")
    if db_business.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.delete_business(db=db, business_id=business_id)