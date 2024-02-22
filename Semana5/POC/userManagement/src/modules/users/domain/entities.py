from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from ....config.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    phoneNumber = Column(String)
    dni = Column(String)
    fullName = Column(String)
    password = Column(String, nullable=True)
    salt = Column(String, nullable=True)
    token = Column(String)
    status = Column(String, nullable=True)
    expireAt = Column(DateTime, nullable=True)
    createdAt = Column(DateTime, server_default=func.now())
    updateAt = Column(DateTime, nullable=True)
