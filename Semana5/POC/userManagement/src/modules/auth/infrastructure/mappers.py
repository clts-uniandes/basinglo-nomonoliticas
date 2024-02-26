from src.seedwork.domain.repositories import Mapper
from src.modules.auth.domain.entities import Credential
from .dto import Credential as CredentialDTO
from src.modules.auth.infrastructure.utils import encrypt_password

class CredentialMapper(Mapper):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def find_type(self) -> type:
        return Credential.__class__

    def entity_to_dto(self, entity: Credential) -> CredentialDTO:
        password, salt = encrypt_password(entity.password)
        credential_dto = CredentialDTO()
        credential_dto.id = str(entity.id)
        credential_dto.createdAt = entity.created_at
        credential_dto.username = entity.username
        credential_dto.password = password
        credential_dto.salt = salt
        return credential_dto

    def dto_to_entity(self, dto: CredentialDTO) -> Credential:
        credential = Credential(id=dto.id, created_at=dto.createdAt, username=dto.username, password=dto.password, salt=dto.salt)        
        return credential
