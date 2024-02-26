from __future__ import annotations

from dataclasses import dataclass, field
from src.modules.users.domain.events import PersonalInfoCreated
from src.seedwork.domain.entities import AgregationRoot

@dataclass
class PersonalInformation(AgregationRoot):
    id_credential: str = field(default=None)
    email: str = field(default=None)
    dni: str = field(default=None)
    fullName: str = field(default=None)
    phoneNumber: str = field(default=None)

    def create_personal_info(self, personal_info: PersonalInformation):
        self.id_credential = personal_info.id_credential
        self.email = personal_info.email
        self.dni = personal_info.dni
        self.fullName = personal_info.fullName
        self.phoneNumber = personal_info.phoneNumber

        self.add_event(PersonalInfoCreated(id_personalInfo=self.id, created_at=self.created_at))






















