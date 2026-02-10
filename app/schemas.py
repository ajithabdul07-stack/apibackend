from pydantic import BaseModel

class ContactCreate(BaseModel):
    full_name: str
    email: str
    phone_number: int
    message: str
