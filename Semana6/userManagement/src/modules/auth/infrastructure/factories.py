
from dataclasses import dataclass

from src.seedwork.domain.factories import Factory
from src.seedwork.domain.repositories import Repository
from src.modules.auth.domain.repositories import CredentialsRepository
from .exceptions import NoImplementationForFactoryTypeException
from .repositories import CredentialsPostgresRepository

@dataclass
class RepoFactory(Factory):
    def create_object(self, obj: type, mapper: any = None) -> Repository:
        if obj == CredentialsRepository.__class__:
            return CredentialsPostgresRepository()
        else:
            raise NoImplementationForFactoryTypeException()
