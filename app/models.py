from sqlalchemy import Column, Integer, String
from .database import Base

class Contact(Base):
    __tablename__ = "contactform"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    message = Column(String, nullable=False)
    

