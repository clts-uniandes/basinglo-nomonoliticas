from dataclasses import dataclass

from src.seedwork.domain.factories import Factory
from src.seedwork.domain.repositories import Repository
from src.transactions.domain.repositories import TransactionRepository
from .exceptions import NoImplementationForFactoryTypeException
from .repositories import TransactionPostgresRepository

@dataclass
class RepoFactory(Factory):
    def create_object(self, obj: type, mapper: any = None) -> Repository:
        if obj == TransactionRepository.__class__:
            return TransactionPostgresRepository()
        else:
            raise NoImplementationForFactoryTypeException()
    
