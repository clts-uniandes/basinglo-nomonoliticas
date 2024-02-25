from __future__ import annotations

import uuid

from dataclasses import dataclass, field
from src.modules.auth.domain.events import CredentialCreated
from src.seedwork.domain.entities import AgregationRoot

@dataclass
class Credential(AgregationRoot):
    username: str = field(default=None)
    password: str = field(default=None)

    def create_credential(self, credential: Credential):
        self.username = credential.username
        self.password = credential.password

        self.add_event(CredentialCreated(id_credential=self.id, created_at=self.created_at))
