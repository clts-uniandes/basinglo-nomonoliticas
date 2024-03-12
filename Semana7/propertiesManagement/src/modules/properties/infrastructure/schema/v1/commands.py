from pulsar.schema import *
from dataclasses import dataclass, field
from src.seedwork.infraestructure.schema.v1.commands import CommandIntegration
 
class CommandUpdatePropertyPayload(CommandIntegration):
    id = String()
    property_size = Float()
    property_type = String()
    total_area_size = Float()
    floors_number = Integer()
    is_parking = Boolean()
    photos_registry = String()
    ubication = String()
    owner_id = String()
 
class CommandUpdateProperty(CommandIntegration):
    data = CommandUpdatePropertyPayload()
