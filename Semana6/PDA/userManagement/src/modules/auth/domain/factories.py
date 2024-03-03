from dataclasses import dataclass

from .entities import Credential
from .rules import PasswordIsValid
from src.seedwork.domain.repositories import Mapper
from src.seedwork.domain.factories import Factory
from src.seedwork.domain.entities import Entity

@dataclass
class CredentialFactory(Factory):
    def create_object(self, obj: any, mapper: Mapper) -> any:
        if isinstance(obj, Entity):
            return mapper.entity_to_dto(obj)
        else:
            credential: Credential = mapper.dto_to_entity(obj)
            self.validate_rule(PasswordIsValid(credential.password))
            return credential
