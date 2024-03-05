from src.seedwork.domain.repositories import Mapper
from src.modules.auth.domain.entities import Credential
from .dto import Credential as CredentialDTO
from src.modules.auth.infrastructure.utils import encrypt_password

from src.modules.auth.domain.events import CredentialCreated, CredentialEvent
from .exceptions import NoImplementationForFactoryTypeException

class EventsCredentialMapper(Mapper):

    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            CredentialCreated: self._entity_to_credential_created
        }

    def is_valid_version(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entity_to_credential_created(self, entity: CredentialCreated, version=LATEST_VERSION):
        def v1(event):
            from .schema.v1.events import UserCreatedEvent
            integration_event = UserCreatedEvent(
                email=str(event.email)
            )
            return integration_event
        if not self.is_valid_version(version):
            raise Exception(f'Version {version} was not able to be proccesed.')
        if version == 'v1':
            return v1(entity)

    def find_type(self) -> type:
        return CredentialEvent.__class__

    def entity_to_dto(self, entity: CredentialEvent, version=LATEST_VERSION) -> CredentialDTO:
        if not entity:
            raise NoImplementationForFactoryTypeException
        func = self.router.get(entity.__class__, None)
        if not func:
            raise NoImplementationForFactoryTypeException
        return func(entity, version=version)

    def dto_to_entity(self, dto: CredentialDTO) -> Credential:
        raise NotImplementedError



class CredentialMapper(Mapper):
    
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
