from pulsar.schema import *
from src.seedwork.infraestructure.schema.v1.events import EventIntegracion

class PropertyUpdatedPayload(Record):
    id = String()
    property_size = Float()
    property_type = String()
    total_area_size = Float()
    floors_number = Integer()
    is_parking = Boolean()
    photos_registry = String()
    ubication = String()
    owner_id = String()

class EventPropertyUpdated(EventIntegracion):
    data = PropertyUpdatedPayload()

class EventPropertyUpdatedFailed(EventIntegracion):
    data = PropertyUpdatedPayload()