from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..deps import get_db, user_dependency

router = APIRouter(
    prefix="/invoices",
    tags=["Invoices"]
)

@router.get("/", response_model=List[schemas.Invoice])
def read_invoices(
    skip: int = 0, 
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(user_dependency)
):
    if current_user.role == "admin":
        invoices = crud.get_invoices(db, skip=skip, limit=limit)
    else:
        # Get invoices for user's orders
        orders = crud.get_orders_by_user(db, user_id=current_user.id)
        invoice_ids = [order.invoice.id for order in orders if order.invoice]
        invoices = db.query(crud.Invoices).filter(crud.Invoices.id.in_(invoice_ids)).all()
    return invoices

@router.get("/{invoice_id}", response_model=schemas.Invoice)
def read_invoice(
    invoice_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(user_dependency)
):
    db_invoice = crud.get_invoice(db, invoice_id=invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    
    # Check if user owns the order associated with this invoice
    if current_user.role != "admin":
        db_order = crud.get_order(db, order_id=db_invoice.order_id)
        if db_order.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not authorized")
    
    return db_invoice

@router.post("/{invoice_id}/pay", response_model=schemas.Invoice)
def mark_invoice_as_paid(
    invoice_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(user_dependency)
):
    db_invoice = crud.get_invoice(db, invoice_id=invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    
    # Check if user owns the order associated with this invoice
    if current_user.role != "admin":
        db_order = crud.get_order(db, order_id=db_invoice.order_id)
        if db_order.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not authorized")
    
    return crud.mark_invoice_as_paid(db=db, invoice_id=invoice_id)