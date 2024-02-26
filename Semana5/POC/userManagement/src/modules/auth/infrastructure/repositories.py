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
        credential_dto = db.session.query(CredentialDTO).filter_by(username=username).first()
        if credential_dto is None:
            raise Exception("Credentials not found")
        return self.credential_factory.create_object(credential_dto, CredentialMapper())

    def get_by_id(self, id: UUID) -> Credential:
        raise NotImplementedError 

    def add(self, credential: Credential):
        old_credential = db.session.query(CredentialDTO).filter_by(username=credential.username).first()
        if old_credential is not None:
            raise Exception('Credential already exist')
        credential_dto = self.credential_factory.create_object(credential, CredentialMapper())
        db.session.add(credential_dto)
