from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..deps import get_db, user_dependency

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)

@router.post("/", response_model=schemas.Payment)
def create_payment(
    payment: schemas.PaymentCreate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(user_dependency)
):
    # Verify the invoice exists
    db_invoice = crud.get_invoice(db, invoice_id=payment.invoice_id)
    if not db_invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    
    # Check if user owns the order associated with this invoice
    if current_user.role != "admin":
        db_order = crud.get_order(db, order_id=db_invoice.order_id)
        if db_order.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not authorized")
    
    return crud.create_payment(db=db, payment=payment)

@router.get("/", response_model=List[schemas.Payment])
def read_payments(
    skip: int = 0, 
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(user_dependency)
):
    if current_user.role == "admin":
        payments = crud.get_payments(db, skip=skip, limit=limit)
    else:
        # Get payments for user's invoices
        orders = crud.get_orders_by_user(db, user_id=current_user.id)
        invoice_ids = [order.invoice.id for order in orders if order.invoice]
        payments = db.query(crud.Payments).filter(crud.Payments.invoice_id.in_(invoice_ids)).all()
    return payments

@router.get("/{payment_id}", response_model=schemas.Payment)
def read_payment(
    payment_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(user_dependency)
):
    db_payment = crud.get_payment(db, payment_id=payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    
    # Check if user owns the invoice associated with this payment
    if current_user.role != "admin":
        db_invoice = crud.get_invoice(db, invoice_id=db_payment.invoice_id)
        db_order = crud.get_order(db, order_id=db_invoice.order_id)
        if db_order.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not authorized")
    
    return db_payment