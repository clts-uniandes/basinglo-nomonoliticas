from __future__ import annotations
import uuid

from dataclasses import dataclass
from src.seedwork.domain.events import DomainEvent
from datetime import datetime

@dataclass
class CredentialCreated(DomainEvent):
    id_credential: uuid.UUID = None
    created_at: datetime = None
