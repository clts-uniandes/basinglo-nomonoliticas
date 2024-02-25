from dataclasses import dataclass

from src.seedwork.domain.factories import Factory
from src.seedwork.domain.repositories import Repository
from src.modules.users.domain.repositories import PersonalInformationRepository
from .exceptions import NoImplementationForFactoryTypeException
from .repositories import PersonalInformationRepository

@dataclass
class RepoFactory(Factory):
    def create_object(self, obj: type, mapper: any = None) -> Repository:
        if obj == PersonalInformationRepository.__class__:
            return PersonalInformationRepository()
        else:
            raise NoImplementationForFactoryTypeException()