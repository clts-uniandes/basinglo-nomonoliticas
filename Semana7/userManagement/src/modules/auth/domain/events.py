from __future__ import annotations
import uuid
from dataclasses import dataclass
from datetime import datetime

from src.seedwork.domain.events import DomainEvent

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

@dataclass
class CredentialNotCreated(DomainEvent):
    username: str = None
    email: str = None
