from dataclasses import dataclass

from src.seedwork.application.commands import Command
from src.modules.properties.application.dto import PropertyAppDTO
from .base import UpdatePropertyBaseHandler

from src.seedwork.application.commands import exec_command as command
from src.modules.properties.domain.entities import Property
from src.seedwork.infraestructure.uow import UnitOfWorkPort
from src.modules.properties.application.mappers import MapperProperty
from src.modules.properties.infrastructure.repositories import PropertyRepository

@dataclass
class UpdateProperty(Command):
    id: str
    property_size: float
    property_type: str
    total_area_size: float
    floors_number: int
    is_parking: bool
    photos_registry: str
    ubication: str
    
class UpdatePropertyHandler(UpdatePropertyBaseHandler):
    def handle(self, command: UpdateProperty):
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
        
        property.update_property(property)
        
        repository = self.repo_factory.create_object(PropertyRepository.__class__)
        
        UnitOfWorkPort.register_batch(repository.update, property, command.id)
        
        UnitOfWorkPort.commit()
        
        
@command.register(UpdateProperty)
def exec_command_update_property(command: UpdateProperty):
    handler = UpdatePropertyHandler()
    handler.handle(command)
