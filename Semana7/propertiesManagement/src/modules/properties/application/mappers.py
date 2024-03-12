from src.seedwork.application.dto import Mapper as AppMap
from src.seedwork.domain.repositories import Mapper as RepoMap
from src.modules.properties.domain.entities import Property
from .dto import PropertyAppDTO

class MapperPropertyDTOJson(AppMap):
    def external_to_dto(self, external: dict) -> PropertyAppDTO:
        property_dto = PropertyAppDTO(
            property_size= external['property_size'],
            property_type= external['property_type'],
            total_area_size= external['total_area_size'],
            floors_number= external['floors_number'],
            is_parking= external['is_parking'],
            photos_registry= external['photos_registry'],
            ubication= external['ubication'],
            owner_id= external['owner_id'],
        )
        return property_dto
    
    def dto_to_external(self, dto: PropertyAppDTO) -> dict:
        return dto.__dict__
    


class MapperProperty(RepoMap):
    
    def find_type(self) -> type:
        return Property.__class__
    
    def entity_to_dto(self, entity: Property) -> PropertyAppDTO:
        return PropertyAppDTO(entity.property_size,entity.property_type,entity.total_area_size,entity.floors_number,entity.is_parking,entity.photos_registry,entity.ubication)
    
    def dto_to_entity(self, dto: PropertyAppDTO) -> Property:
        property = Property()
        property.property_size = dto.property_size
        property.property_type = dto.property_type
        property.total_area_size = dto.total_area_size
        property.floors_number = dto.floors_number
        property.is_parking = dto.is_parking
        property.photos_registry = dto.photos_registry
        property.ubication = dto.ubication
        property.owner_id = dto.owner_id
        
        return property