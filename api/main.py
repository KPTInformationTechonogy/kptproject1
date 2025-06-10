from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from api.routes import contact



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
    
app.include_router(contact.router, prefix="/api")
