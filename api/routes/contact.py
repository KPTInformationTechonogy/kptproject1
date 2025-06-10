# backend/api/routes/contact.py
from fastapi import APIRouter, Form, HTTPException
import smtplib
from email.mime.text import MIMEText

router = APIRouter()

@router.post("/contact")
def send_contact_email(
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):
    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    msg = MIMEText(body)
    msg["Subject"] = "New Contact Form Submission"
    msg["From"] = "aliumukhtar123@gmail.vom"
    msg["To"] = "kptinformationtechnology@example.com"

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login("kptinformationtechnology@gmail.com", "Kpt@003")
            server.send_message(msg)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"message": "Email sent successfully"}
