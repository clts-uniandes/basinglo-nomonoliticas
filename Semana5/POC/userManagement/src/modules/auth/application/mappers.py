from src.seedwork.application.dto import Mapper as AppMap
from src.seedwork.domain.repositories import Mapper as RepMap
from src.modules.auth.domain.entities import Credential
from .dto import CredentialAppDTO

class MapperAuthDTOJson(AppMap):
    def external_to_dto(self, externo: dict) -> CredentialAppDTO:
        credential_dto = CredentialAppDTO(
            username= externo['username'],
            password= externo['password'],
            salt= ''
        )
        return credential_dto

    def dto_to_external(self, dto: CredentialAppDTO) -> dict:
        return dto.__dict__


class MapperCredential(RepMap):

    def find_type(self) -> type:
        return Credential.__class__
        
    def entity_to_dto(self, entity: Credential) -> CredentialAppDTO:
        return CredentialAppDTO(entity.username, entity.password, entity.salt)

    def dto_to_entity(self, dto: CredentialAppDTO) -> Credential:
        credential = Credential()
        credential.username = dto.username
        credential.password = dto.password
        credential.salt = dto.salt
        return credential



