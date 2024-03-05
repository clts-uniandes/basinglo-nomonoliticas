from __future__ import annotations
import uuid

from dataclasses import dataclass
from src.seedwork.domain.events import DomainEvent
from datetime import datetime

class CredentialEvent(DomainEvent):
    ...

@dataclass
class CredentialCreated(CredentialEvent):
    id_credential: uuid.UUID = None
    created_at: datetime = None
    email: str = None
    dni: str = None
    fullName: str = None
    phoneNumber: str = None
