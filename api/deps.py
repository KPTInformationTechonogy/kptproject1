from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from passlib.context import CryptContext
import os
from .database import SessionLocal, get_db
from .models import Users

load_dotenv()

# Validate environment variables
SECRET_KEY = os.getenv('AUTH_SECRET_KEY')
ALGORITHM = os.getenv('AUTH_ALGORITHM')

if not SECRET_KEY or not ALGORITHM:
    raise ValueError("Missing AUTH_SECRET_KEY or AUTH_ALGORITHM in environment variables")

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

async def get_current_user(
    token: str = Depends(oauth2_bearer),
    db: Session = Depends(get_db)
) -> Users:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('sub')
        user_id: int = payload.get('id')
        if email is None or user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = db.query(Users).filter(Users.id == user_id).first()
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
    current_user: Users = Depends(get_current_user)
) -> Users:
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )
    return current_user

def admin_required(
    current_user: Users = Depends(get_current_active_user)
) -> Users:
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required"
        )
    return current_user

# Dependency type aliases
user_dependency = Annotated[Users, Depends(get_current_active_user)]
admin_dependency = Annotated[Users, Depends(admin_required)]

__all__ = [
    "get_db",
    "get_current_user",
    "get_current_active_user",
    "admin_required",
    "user_dependency",
    "admin_dependency",
    "bcrypt_context",
    "oauth2_bearer"
]