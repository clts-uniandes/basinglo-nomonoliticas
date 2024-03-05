from uuid import uuid4

from src.config.db import db

from sqlalchemy import Column, DateTime,  String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

Base = db.declarative_base()

class Credential(db.Model):
    __tablename__ = "credentials"

    id = Column(UUID(as_uuid=True), primary_key=True)#, default=uuid4
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=True)
    salt = Column(String, nullable=True)
    createdAt = Column(DateTime, server_default=func.now())
    updateAt = Column(DateTime, nullable=True)
