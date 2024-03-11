from src.config.db import db
from uuid import UUID

from src.modules.properties.domain.repositories import PropertyRepository
from src.modules.properties.domain.factories import PropertyFactory
from src.modules.properties.domain.entities import Property
from .mappers import PropertyMapper
from .dto import Property as PropertyDTO
from .dispatchers import Dispatcher
from src.modules.properties.infrastructure.schema.v1.events import EventPropertyUpdated, EventPropertyUpdatedFailed, PropertyUpdatedPayload

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

    def update(self, property: Property, property_id):
        property_dto = self._property_factory.create_object(
            property, PropertyMapper()
        )
        existing_property_dto = db.session.query(PropertyDTO).filter_by(id=property_id).first()
        if existing_property_dto is None:
            raise Exception("Property not found")
        if property_dto.property_size is not None:
            existing_property_dto.property_size = property_dto.property_size
        if property_dto.property_type is not None:
            existing_property_dto.property_type = property_dto.property_type
        if property_dto.total_area_size is not None:
            existing_property_dto.total_area_size = property_dto.total_area_size
        if property_dto.floors_number is not None:
            existing_property_dto.floors_number = property_dto.floors_number
        if property_dto.is_parking is not None:
            existing_property_dto.is_parking = property_dto.is_parking
        if property_dto.photos_registry is not None:
            existing_property_dto.photos_registry = property_dto.photos_registry
        if property_dto.ubication is not None:
            existing_property_dto.ubication = property_dto.ubication
        if property_dto.owner_id is not None:
            existing_property_dto.owner_id = property_dto.owner_id
        try:
            db.session.commit()
            dispatcher = Dispatcher()
            payload = PropertyUpdatedPayload(id = property_id, owner_id = property_dto.owner_id)
            event_integration = EventPropertyUpdated(data=payload)
            dispatcher.publish_menssage(event_integration, 'update-property-topic')
        except Exception as e:
            dispatcher = Dispatcher()
            payload = PropertyUpdatedPayload(id = property_id, owner_id = property_dto.owner_id)
            event_integration = EventPropertyUpdatedFailed(data=payload)
            dispatcher.publish_menssage(event_integration, 'update-property-topic')
