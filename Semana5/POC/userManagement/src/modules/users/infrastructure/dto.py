from uuid import uuid4

from src.config.db import db

from sqlalchemy import Column, DateTime,  String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

Base = db.declarative_base()

class PersonalInformation(db.Model):
    __tablename__ = "personalInformation"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    userName = Column(String, nullable=False, unique=True)
    password = Column(String)
    email = Column(String)
    dni = Column(int, nullable=False)
    fullName = Column(String, nullable=False)
    phoneNumber = Column(String)
    createdAt = Column(DateTime, server_default=func.now())    