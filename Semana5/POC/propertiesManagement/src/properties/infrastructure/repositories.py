from src.config.db import db
from uuid import UUID

from src.properties.domain.repositories import PropertyRepository
from src.properties.domain.factories import PropertyFactory
from src.properties.domain.entities import Property
from .mappers import PropertyMapper

class PropertyPostgresRepository(PropertyRepository):

    def __init__(self):
        self._property_factory: PropertyFactory = (
            PropertyFactory()
        )

    @property
    def credential_factory(self):
        return self._property_factory
    
    def get_by_id(self, id: UUID) -> Property:
        raise NotImplementedError
    
    def add(self, property: Property):
        property_dto = self._property_factory.create_object(
            property, PropertyMapper()
        )
        db.session.add(property_dto)