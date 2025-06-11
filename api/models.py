from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime, func, Boolean
from sqlalchemy.orm import relationship
from .database import Base
from enum import Enum as PyEnum

class InvoiceStatus(PyEnum):
    PENDING = "pending"
    PAID = "paid"
    CANCELLED = "cancelled"

class PaymentStatus(PyEnum):
    PENDING = "pending"
    SUCCESSFUL = "successful"
    FAILED = "failed"

class BaseMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_active = Column(Boolean, default=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)


class Users(Base, BaseMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey("businesses.id"))
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, index=True, nullable=False)
    role = Column(String, index=True, nullable=False)

    business = relationship("Businesses", back_populates="users")
    orders = relationship("Orders", back_populates="user", cascade="all, delete-orphan")
    cart_items = relationship("Cart", back_populates="user", cascade="all, delete-orphan")

class Businesses(Base, BaseMixin):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(Integer, unique=True, index=True, nullable=False)
    
    users = relationship("Users", back_populates="business", cascade="all, delete-orphan")
    products = relationship("Products", back_populates="business", cascade="all, delete-orphan")  # ✅ Added

class Products(Base, BaseMixin):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey("businesses.id"))  # ✅ Added
    name = Column(String, index=True, nullable=False)
    size = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=False)
    category = Column(String, index=True, nullable=False)
    quantity = Column(Integer, index=True, nullable=False)
    price = Column(Integer, index=True, nullable=False)
    image_url = Column(String, index=True, nullable=False)

    business = relationship("Businesses", back_populates="products")  # ✅ Added
    orders = relationship("Orders", back_populates="product", cascade="all, delete-orphan")
    cart_items = relationship("Cart", back_populates="product", cascade="all, delete-orphan")


class Orders(Base, BaseMixin):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, index=True, nullable=False)
    total_price = Column(Integer, index=True, nullable=False)

    user = relationship("Users", back_populates="orders")
    product = relationship("Products", back_populates="orders")
    invoice = relationship("Invoices", back_populates="order", uselist=False, cascade="all, delete-orphan")

class Cart(Base, BaseMixin):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, index=True, nullable=False)

    user = relationship("Users", back_populates="cart_items")
    product = relationship("Products", back_populates="cart_items")

class Invoices(Base, BaseMixin):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    invoice_number = Column(String, unique=True, index=True, nullable=False)
    total_amount = Column(Integer, index=True, nullable=False)
    status = Column(Enum(InvoiceStatus), default=InvoiceStatus.PENDING, nullable=False)

    order = relationship("Orders", back_populates="invoice")
    payments = relationship("Payments", back_populates="invoice", cascade="all, delete-orphan")

class Payments(Base, BaseMixin):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))
    amount = Column(Integer, index=True, nullable=False)
    payment_method = Column(String, index=True, nullable=False)
    status = Column(Enum(PaymentStatus), default=PaymentStatus.PENDING, nullable=False)

    invoice = relationship("Invoices", back_populates="payments")
