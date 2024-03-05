from src.seedwork.application.dto import Mapper as AppMap
from src.seedwork.domain.repositories import Mapper as RepoMap
from src.modules.auth.domain.entities import Credential
from .dto import CredentialAppDTO

class MapperAuthDTOJson(AppMap):
    def external_to_dto(self, external: dict) -> CredentialAppDTO:
        credential_dto = CredentialAppDTO(
            username= external['username'],
            password= external['password'],
            email= external['email'],
            dni= external['dni'],
            fullName= external['fullName'],
            phoneNumber= external['phoneNumber'],
            salt=''
        )
        return credential_dto

    def dto_to_external(self, dto: CredentialAppDTO) -> dict:
        return dto.__dict__


class MapperCredential(RepoMap):

    def find_type(self) -> type:
        return Credential.__class__
        
    def entity_to_dto(self, entity: Credential) -> CredentialAppDTO:
        return CredentialAppDTO(entity.username, entity.password, entity.email, entity.dni, entity.fullName, entity.phoneNumber, entity.salt)

    def dto_to_entity(self, dto: CredentialAppDTO) -> Credential:
        credential = Credential()
        credential.username = dto.username
        credential.password = dto.password
        credential.salt = ""
        credential.email = dto.email
        credential.dni = dto.dni
        credential.fullName = dto.fullName
        credential.phoneNumber = dto.phoneNumber

        return credential



