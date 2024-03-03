from __future__ import annotations
import uuid

from dataclasses import dataclass
from src.seedwork.domain.events import DomainEvent
from datetime import datetime

@dataclass
class PersonalInfoCreated(DomainEvent):
    id_personalInfo: uuid.UUID = None
    created_at: datetime = None
