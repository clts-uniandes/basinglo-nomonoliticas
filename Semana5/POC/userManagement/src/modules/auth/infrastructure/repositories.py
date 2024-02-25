from src.config.db import db

from src.modules.auth.domain.repositories import CredentialsRepository
from src.modules.auth.domain.entities import Credential
from src.modules.auth.domain.factories import CredentialFactory

from .dto import Credential as CredentialDTO
from .mappers import CredentialMapper
from uuid import UUID

class CredentialsPostgresRepository(CredentialsRepository):

    def __init__(self):
        self._credential_factory: CredentialFactory = CredentialFactory()

    @property
    def credential_factory(self):
        return self._credential_factory
    
    def get_by_username(self, username: str) -> Credential:
        session = db.session
        credential_dto = session.query(CredentialDTO).filter_by(username=username).one()
        return self.credential_factory.create_object(credential_dto, CredentialMapper())

    def get_by_id(self, id: UUID) -> Credential:
        raise NotImplementedError 

    def add(self, credential: Credential):
        session = db.session
        credential_dto = self.credential_factory.create_object(credential, CredentialMapper())
        session.add(credential_dto)
