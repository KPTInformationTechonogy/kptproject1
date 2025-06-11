# schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

# Enum definitions
class InvoiceStatus(str, Enum):
    pending = "pending"
    paid = "paid"
    cancelled = "cancelled"

class PaymentStatus(str, Enum):
    pending = "pending"
    successful = "successful"
    failed = "failed"

# Common mixin
class TimestampMixin(BaseModel):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]
    is_active: Optional[bool] = True

# Business
class BusinessBase(BaseModel):
    name: str
    description: str
    email: str
    phone_number: int

class BusinessCreate(BusinessBase):
    pass

class BusinessUpdate(BusinessBase):
    is_active: Optional[bool]

class Business(BusinessBase, TimestampMixin):
    id: int

    class Config:
        orm_mode = True

# User
class UserBase(BaseModel):
    name: str
    email: str
    password: str
    role: str

class UserCreate(UserBase):
    business_id: int

class UserUpdate(UserBase):
    is_active: Optional[bool]

class User(UserBase, TimestampMixin):
    id: int
    business_id: int

    class Config:
        orm_mode = True

# Product
class ProductBase(BaseModel):
    name: str
    size: str
    description: str
    category: str
    quantity: int
    price: int
    image_url: str

class ProductCreate(ProductBase):
    business_id: int

class ProductUpdate(ProductBase):
    is_active: Optional[bool]

class Product(ProductBase, TimestampMixin):
    id: int
    business_id: int

    class Config:
        orm_mode = True

# Order
class OrderBase(BaseModel):
    quantity: int
    total_price: int

class OrderCreate(OrderBase):
    user_id: int
    product_id: int

class OrderUpdate(OrderBase):
    is_active: Optional[bool]

class Order(OrderBase, TimestampMixin):
    id: int
    user_id: int
    product_id: int

    class Config:
        orm_mode = True

# Cart
class CartBase(BaseModel):
    quantity: int

class CartCreate(CartBase):
    user_id: int
    product_id: int

class CartUpdate(CartBase):
    is_active: Optional[bool]

class Cart(CartBase, TimestampMixin):
    id: int
    user_id: int
    product_id: int

    class Config:
        orm_mode = True

# Invoice
class InvoiceBase(BaseModel):
    invoice_number: str
    total_amount: int
    status: InvoiceStatus

class InvoiceCreate(InvoiceBase):
    order_id: int

class InvoiceUpdate(InvoiceBase):
    is_active: Optional[bool]

class Invoice(InvoiceBase, TimestampMixin):
    id: int
    order_id: int

    class Config:
        orm_mode = True

# Payment
class PaymentBase(BaseModel):
    amount: int
    payment_method: str
    status: PaymentStatus

class PaymentCreate(PaymentBase):
    invoice_id: int

class PaymentUpdate(PaymentBase):
    is_active: Optional[bool]

class Payment(PaymentBase, TimestampMixin):
    id: int
    invoice_id: int

    class Config:
        orm_mode = True
class ProductBase(BaseModel):
    name: str
    size: str
    description: str
    category: str
    quantity: int
    price: int
    image_url: str

# Creation schema
class ProductCreate(ProductBase):
    business_id: int

# Update schema
class ProductUpdate(ProductBase):
    is_active: Optional[bool] = True

# Response schema
class Product(ProductBase):
    id: int
    business_id: int
    is_active: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True