from uuid import uuid4

from src.config.db import db

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

Base = db.declarative_base()

class User(db.Model):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    credentialId = Column(UUID(as_uuid=True), nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    phoneNumber = Column(String)
    dni = Column(String)
    fullName = Column(String)
    status = Column(String, nullable=True)
    expireAt = Column(DateTime, nullable=True)
    createdAt = Column(DateTime, server_default=func.now())
    updateAt = Column(DateTime, nullable=True)

class PersonalInformation(db.Model):
    __tablename__ = "personalInformation"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    userName = Column(String)
    password = Column(String)
    email = Column(String)
    dni = Column(int)
    fullName = Column(String)
    phoneNumber = Column(String)
    createdAt = Column(DateTime, server_default=func.now())
