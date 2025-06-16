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


    

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    products = db.query(models.Products).all()
    return {"success":products}

@app.get("/businesses")
def get_products(db: Session = Depends(get_db)):
    businesses = db.query(models.Businesses).all()
    return {"success":businesses}

@app.get("/product")
def get_products(db: Session = Depends(get_db)):
    products = db.query(models.Products).filter(models.Products.is_active == True).all()
    return products



@app.post("/create_products", status_code=status.HTTP_201_CREATED)
def create_products(create_products: schemas.ProductCreate, db: Session = Depends(get_db)):
    existing_product = db.query(models.Products).filter(models.Products.name == create_products.name).first()
    if existing_product:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="product is available")
    new_product = models.Products(**create_products.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

    
@app.post("/create_business", status_code=status.HTTP_201_CREATED)
def create_business(create_business: schemas.BusinessCreate, db: Session = Depends(get_db)):
    # Check if a business with the same email already exists
    existing_business = db.query(models.Businesses).filter(models.Businesses.email == create_business.email).first()
    if existing_business:
        raise HTTPException(
            status_code=status.HTTP_302_FOUND,
            detail="Business with this email already exists"
        )
    
    # Create a new business
    new_business = models.Businesses(**create_business.dict())
    db.add(new_business)
    db.commit()
    db.refresh(new_business)
    return new_business

@app.put("/new_product/{id}", status_code=status.HTTP_200_OK)
def update_products(id: int, updated_products: schemas.ProductUpdate, db: Session = Depends(get_db)):
    product_query = db.query(models.Products).filter(models.Products.id == id)
    product = product_query.first()

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {id} was not found"
        )

    product_query.update(updated_products.dict(), synchronize_session=False)
    db.commit()
    db.refresh(product)

    return product
    