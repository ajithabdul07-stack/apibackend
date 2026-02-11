from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from .database import SessionLocal
# from .models import Contact
# from .schemas import ContactCreate
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart




router = APIRouter()

def Send_mail(datas):
    password = "Vaqeel@123"
    email = "abdulvaqeel9636@gmail.com"
    app_password = "cmko rofn dmrm aase"

    html_content = f"""
<html>
  <body>
    <h2>User Details Submission</h2>
    <p><b>Name:</b> {datas.full_name}</p>
    <p><b>Contact:</b> {datas.phone_number}</p>
    <p><b>Email:</b> {datas.email}</p>
    <p><b>Message:</b> {datas.message}</p>
    <hr>
    <p>Sent via automated service.</p>
  </body>
</html>
"""
    
    msg = MIMEMultipart("alternative")
    msg["subject"] = "Below is my details:"
    msg["from"] = email
    msg["to"] = "vaqeel@vs.sa"

    msg.attach(MIMEText(html_content, "html"))
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(email,app_password)
            server.sendmail(email, "vaqeel@vs.sa",msg.as_string())
            print("Mail send successfully")
    except smtplib.SMTPAuthenticationError as e:
        print(e)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

@router.post("/contactform")
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    new_contact = Contact(
        full_name=contact.full_name,
        email=contact.email,
        phone_number=contact.phone_number,
        message=contact.message
    )
    Send_mail(new_contact)
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return {"message": "Contact saved successfully"}

@router.get("/")
def Check():

    return {"message":"Code worked"}

