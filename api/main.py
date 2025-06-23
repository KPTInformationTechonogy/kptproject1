from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status, Depends
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
import time
from .database import Base, engine, SessionLocal, get_db
from . import models, schemas
from .routers import businesses, carts, invoices, orders, payments, users, products, auth
from .deps import user_dependency
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


    

@app.get("/protected-route")
async def protected_route(user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"message": f"Hello {user.name}", "user_id": user.id}



Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(businesses.router)
app.include_router(products.router)
app.include_router(orders.router)
app.include_router(carts.router)
app.include_router(invoices.router)
app.include_router(payments.router)
    

app.include_router(auth.router)