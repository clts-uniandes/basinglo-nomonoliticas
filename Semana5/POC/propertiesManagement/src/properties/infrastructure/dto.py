from uuid import uuid4

from src.config.db import db

from sqlalchemy import Column, DateTime,  String, Float, Boolean, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

Base = db.declarative_base()

class Property(db.Model):
    __tablename__ = "properties"

    id = Column(UUID(as_uuid=True), primary_key=True)
    property_size = Column(Float, nullable=True)
    total_area_size = Column(Float, nullable=True)
    floors_number = Column(Integer, nullable=True)
    is_parking = Column(Boolean, nullable=True)
    photos_registry = Column(String, nullable=True)
    ubication = Column(String, nullable=True)
    createdAt = Column(DateTime, server_default=func.now())


