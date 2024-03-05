from dataclasses import dataclass

from .entities import Transaction
from src.seedwork.domain.repositories import Mapper
from src.seedwork.domain.factories import Factory
from src.seedwork.domain.entities import Entity

@dataclass
class TransactionFactory(Factory):
    def create_object(self, obj: any, mapper: Mapper = None) -> any:
        if isinstance(obj, Entity):
            return mapper.entity_to_dto(obj)
        else:
            transaction: Transaction = mapper.dto_to_entity(obj)
            return transaction