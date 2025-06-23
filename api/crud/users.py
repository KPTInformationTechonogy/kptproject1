from ..models import Users
from ..schemas import UserCreate, UserUpdate
from sqlalchemy.orm import Session
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, user_id: int):
    return db.query(Users).filter(Users.id == user_id, Users.is_active == True).first()

def get_user_by_email(db: Session, email: str):
    return db.query(Users).filter(Users.email == email, Users.is_active == True).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Users).filter(Users.is_active == True).offset(skip).limit(limit).all()



def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = Users(
        name=user.name,
        email=user.email,
        password=hashed_password,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    
    update_data = user.dict(exclude_unset=True)
    if "password" in update_data:
        update_data["password"] = pwd_context.hash(update_data["password"])
    
    for field in update_data:
        setattr(db_user, field, update_data[field])
    
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    
    db_user.is_active = False
    db_user.deleted_at = func.now()
    db.commit()
    return db_user