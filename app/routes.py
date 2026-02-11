from fastapi import APIRouter
from pydantic import BaseModel
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

router = APIRouter()

# Request Model
class ContactCreate(BaseModel):
    full_name: str
    email: str
    phone_number: str
    message: str


def Send_mail(datas):
    email = "abdulvaqeel9636@gmail.com"
    app_password = "cmko rofn dmrm aase"   # Gmail App Password

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
    msg["Subject"] = "Below is my details:"
    msg["From"] = email
    msg["To"] = "vaqeel@vs.sa"

    msg.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(email, app_password)
            server.sendmail(email, "vaqeel@vs.sa", msg.as_string())
        return True
    except Exception as e:
        print("Mail Error:", e)
        return False


# POST - Send Mail
@router.post("/contactform")
def create_contact(contact: ContactCreate):
    status = Send_mail(contact)

    if status:
        return {"message": "Mail sent successfully"}
    else:
        return {"message": "Mail sending failed"}


# GET - First URL Check
@router.get("/")
def Check():
    return {"message": "Code worked"}
