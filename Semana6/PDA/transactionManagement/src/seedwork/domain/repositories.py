from abc import ABC, abstractmethod
from uuid import UUID
from .entities import Entity

class Repository(ABC):
    @abstractmethod
    def get_by_id(self, id: UUID) -> Entity:
        ...

    @abstractmethod
    def add(self, entity: Entity):
        ...
    @abstractmethod
    def addAsincronic(self, entity: Entity):
        ...

class Mapper(ABC):
    @abstractmethod
    def find_type(self) -> type:
        ...

    @abstractmethod
    def entity_to_dto(self, entity: Entity) -> any:
        ...

    @abstractmethod
    def dto_to_entity(self, dto: any) -> Entity:
        ...
