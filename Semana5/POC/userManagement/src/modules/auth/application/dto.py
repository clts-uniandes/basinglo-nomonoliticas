from dataclasses import dataclass, field
from ....seedwork.application.dto import DTO

@dataclass(frozen=True)
class CredentialAppDTO(DTO):
    username: str
    password: str
