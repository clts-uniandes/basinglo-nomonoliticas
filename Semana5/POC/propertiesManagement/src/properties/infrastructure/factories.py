from dataclasses import dataclass

from src.seedwork.domain.factories import Factory
from src.seedwork.domain.repositories import Repository
from src.properties.domain.repositories import PropertyRepository
from .exceptions import NoImplementationForFactoryTypeException
from .repositories import PropertyPostgresRepository

@dataclass
class RepoFactory(Factory):
    def create_object(self, obj: type, mapper: any = None) -> Repository:
        if obj == PropertyRepository.__class__:
            return PropertyPostgresRepository()
        else:
            raise NoImplementationForFactoryTypeException()
    
