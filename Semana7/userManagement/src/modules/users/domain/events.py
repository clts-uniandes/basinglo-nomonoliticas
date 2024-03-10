from __future__ import annotations
import uuid
from dataclasses import dataclass
from datetime import datetime

from src.seedwork.domain.events import DomainEvent

class PersonalInfoEvent(DomainEvent):
    ...

@dataclass
class PersonalInfoCreated(PersonalInfoEvent):
    id_credential: uuid.UUID = None
    email: str = None
    created_at: datetime = None

@dataclass
class PersonalInfoNotCreated(DomainEvent):
    id_credential: uuid.UUID = None