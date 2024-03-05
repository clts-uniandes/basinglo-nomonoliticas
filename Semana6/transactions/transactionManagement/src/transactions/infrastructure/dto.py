from uuid import uuid4

from src.config.db import db

from sqlalchemy import Column, DateTime,  String, Float, Boolean, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

Base = db.declarative_base()

class Transaction(db.Model):
    __tablename__ = "transactions"

    id = Column(UUID(as_uuid=True), primary_key=True)
    dni_landlord = Column(String, nullable=True)
    dni_tenant = Column(String, nullable=True)
    monetary_value = Column(Float, nullable=True)
    type_lease = Column(String, nullable=True)
    contract_initial_date = Column(DateTime, nullable=True)
    contract_final_date = Column(DateTime, nullable=True)    
    createdAt = Column(DateTime, server_default=func.now())


