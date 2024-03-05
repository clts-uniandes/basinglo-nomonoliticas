from __future__ import annotations

from dataclasses import dataclass, field
from src.modules.auth.domain.events import CredentialCreated
from src.seedwork.domain.entities import AgregationRoot


@dataclass
class Credential(AgregationRoot):
    username: str = field(default=None)
    password: str = field(default=None)
    salt: str = field(default=None)
    email: str = field(default=None)
    dni: str = field(default=None)
    fullName: str = field(default=None)
    phoneNumber: str = field(default=None)

    def create_credential(self, credential: Credential):
        self.username = credential.username
        self.password = credential.password
        self.email = credential.email
        self.dni = credential.dni
        self.fullName = credential.fullName
        self.phoneNumber = credential.phoneNumber

        self.salt = ""

        self.add_event(
            CredentialCreated(
                id_credential=self.id,
                created_at=self.created_at,
                email=self.email,
                dni=self.dni,
                fullName=self.fullName,
                phoneNumber=self.phoneNumber,
            )
        )
