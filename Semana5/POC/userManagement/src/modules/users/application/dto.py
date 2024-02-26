from dataclasses import dataclass, field
from src.seedwork.application.dto import DTO

@dataclass(frozen=True)
class PersonalInformationAppDTO(DTO):
    id_credential: str
    email: str
    dni: str
    fullName: str
    phoneNumber: str
