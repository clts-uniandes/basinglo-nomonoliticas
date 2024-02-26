from uuid import uuid4

from src.config.db import db

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

Base = db.declarative_base()

class PersonalInformation(db.Model):
    __tablename__ = "personalinformation"
    
    id = Column(UUID(as_uuid=True), primary_key=True)
    credentialId = Column(UUID(as_uuid=True), unique=True)
    email = Column(String)
    dni = Column(String, nullable=False)
    fullName = Column(String, nullable=False)
    phoneNumber = Column(String)