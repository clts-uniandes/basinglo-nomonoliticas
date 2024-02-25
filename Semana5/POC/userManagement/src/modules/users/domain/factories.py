from dataclasses import dataclass

from .entities import PersonalInformation
from src.seedwork.domain.repositories import Mapper
from src.seedwork.domain.factories import Factory
from src.seedwork.domain.entities import Entity

@dataclass
class PersonalInformationFactory(Factory):
    def create_object(self, obj: any, mapper: Mapper) -> any:
        if isinstance(obj, Entity):
            return mapper.entity_to_dto(obj)
        else:
            personal_information: PersonalInformation = mapper.dto_to_entity(obj)
            return personal_information