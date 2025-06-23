from ..models import Invoices, InvoiceStatus
from ..schemas import InvoiceCreate, InvoiceUpdate
from sqlalchemy.orm import Session

def get_invoice(db: Session, invoice_id: int):
    return db.query(Invoices).filter(Invoices.id == invoice_id, Invoices.is_active == True).first()

def get_invoices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Invoices).filter(Invoices.is_active == True).offset(skip).limit(limit).all()

def get_invoices_by_order(db: Session, order_id: int):
    return db.query(Invoices).filter(Invoices.order_id == order_id, Invoices.is_active == True).first()

def create_invoice(db: Session, invoice: InvoiceCreate):
    db_invoice = Invoices(
        order_id=invoice.order_id,
        invoice_number=invoice.invoice_number,
        total_amount=invoice.total_amount,
        status=invoice.status
    )
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def update_invoice(db: Session, invoice_id: int, invoice: InvoiceUpdate):
    db_invoice = get_invoice(db, invoice_id)
    if not db_invoice:
        return None
    
    update_data = invoice.dict(exclude_unset=True)
    for field in update_data:
        setattr(db_invoice, field, update_data[field])
    
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def delete_invoice(db: Session, invoice_id: int):
    db_invoice = get_invoice(db, invoice_id)
    if not db_invoice:
        return None
    
    db_invoice.is_active = False
    db_invoice.deleted_at = func.now()
    db.commit()
    return db_invoice

def mark_invoice_as_paid(db: Session, invoice_id: int):
    db_invoice = get_invoice(db, invoice_id)
    if not db_invoice:
        return None
    
    db_invoice.status = InvoiceStatus.PAID
    db.commit()
    db.refresh(db_invoice)
    return db_invoice