from ..models import Payments, PaymentStatus
from ..schemas import PaymentCreate, PaymentUpdate
from sqlalchemy.orm import Session

def get_payment(db: Session, payment_id: int):
    return db.query(Payments).filter(Payments.id == payment_id, Payments.is_active == True).first()

def get_payments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Payments).filter(Payments.is_active == True).offset(skip).limit(limit).all()

def get_payments_by_invoice(db: Session, invoice_id: int):
    return db.query(Payments).filter(Payments.invoice_id == invoice_id, Payments.is_active == True).all()

def create_payment(db: Session, payment: PaymentCreate):
    db_payment = Payments(
        invoice_id=payment.invoice_id,
        amount=payment.amount,
        payment_method=payment.payment_method,
        status=payment.status
    )
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    
    # Update invoice status if payment is successful
    if db_payment.status == PaymentStatus.SUCCESSFUL:
        invoice = get_invoice(db, payment.invoice_id)
        if invoice:
            invoice.status = InvoiceStatus.PAID
            db.commit()
            db.refresh(invoice)
    
    return db_payment

def update_payment(db: Session, payment_id: int, payment: PaymentUpdate):
    db_payment = get_payment(db, payment_id)
    if not db_payment:
        return None
    
    update_data = payment.dict(exclude_unset=True)
    for field in update_data:
        setattr(db_payment, field, update_data[field])
    
    db.commit()
    db.refresh(db_payment)
    return db_payment

def delete_payment(db: Session, payment_id: int):
    db_payment = get_payment(db, payment_id)
    if not db_payment:
        return None
    
    db_payment.is_active = False
    db_payment.deleted_at = func.now()
    db.commit()
    return db_payment