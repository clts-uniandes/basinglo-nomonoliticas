from dataclasses import dataclass, field
from src.seedwork.application.dto import DTO

@dataclass(frozen=True)
class CredentialAppDTO(DTO):
    username: str
    password: str
    email: str
    dni: str
    fullName: str
    phoneNumber: str
    salt: str
