from dataclasses import dataclass

from src.seedwork.application.commands import Command
from src.modules.properties.application.dto import PropertyAppDTO
from .base import SavePropertyBaseHandler

from src.seedwork.application.commands import exec_command as command
from src.modules.properties.domain.entities import Property
from src.seedwork.infraestructure.uow import UnitOfWorkPort
from src.modules.properties.application.mappers import MapperProperty
from src.modules.properties.infrastructure.repositories import PropertyRepository

@dataclass
class SaveProperty(Command):
    property_size: float
    property_type: str
    total_area_size: float
    floors_number: int
    is_parking: bool
    photos_registry: str
    ubication: str
    
class SavePropertyHandler(SavePropertyBaseHandler):
    def handle(self, command: SaveProperty):
        property_dto = PropertyAppDTO(
            property_size=command.property_size,
            property_type=command.property_type,
            total_area_size=command.total_area_size,
            floors_number=command.floors_number,
            is_parking=command.is_parking,
            photos_registry=command.photos_registry,
            ubication=command.ubication
        )
        
        # evaluate
        property: Property = self.property_factory.create_object(
            property_dto, MapperProperty()
        )
        
        property.create_property(property)
        
        repository = self.repo_factory.create_object(PropertyRepository.__class__)
        
        UnitOfWorkPort.register_batch(repository.add, property)
        
        UnitOfWorkPort.commit()
        
        
@command.register(SaveProperty)
def exec_command_save_property(command: SaveProperty):
    handler = SavePropertyHandler()
    handler.handle(command)
        