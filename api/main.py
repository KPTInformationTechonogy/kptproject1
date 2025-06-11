from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status, Depends
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
import time
from .database import Base, engine, SessionLocal, get_db
from . import models, schemas
from api.routes import contact
from typing import Optional
from typing import List
from datetime import datetime




Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Database connection
try:
    conn = psycopg2.connect(host="localhost", database="ecommerce", user="postgres", password="Aaliiyuu123", cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("Database connection successful")
except Exception as error:
    print("Database connection failed")
    print(f"Error: {error}")
    time.sleep(2)



# Shared properties


    
class Product(BaseModel):
    id: int
    name: str
    size: str
    description: str
    quantity: int
    price: int
    




@app.get("/products", response_model=List[schemas.Product])
def get_products(db: Session = Depends(get_db)):
    products = db.query(models.Products).filter(models.Products.is_active == True).all()
    return products
