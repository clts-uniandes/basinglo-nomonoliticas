from src.seedwork.domain.repositories import Mapper
from src.modules.properties.domain.entities import Property
from .dto import Property as PropertyDTO

class PropertyMapper(Mapper):

    def find_type(self) -> type:
        return Property.__class__
    
    def entity_to_dto(self, entity: Property) -> PropertyDTO:
        property_dto = PropertyDTO()
        property_dto.id = str(entity.id)
        property_dto.property_size = entity.property_size
        property_dto.property_type = entity.property_type
        property_dto.total_area_size = entity.total_area_size
        property_dto.floors_number = entity.floors_number
        property_dto.is_parking = entity.is_parking
        property_dto.photos_registry = entity.photos_registry
        property_dto.ubication = entity.ubication
        property_dto.createdAt = entity.created_at
        return property_dto
    
    def dto_to_entity(self, dto: PropertyDTO) -> PropertyDTO:
        property = Property(id=dto.id, property_size=dto.property_size, property_type=dto.property_type, total_area_size=dto.total_area_size, floors_number=dto.floors_number,
                             is_parking=dto.is_parking, photos_registry=dto.photos_registry, ubication=dto.ubication, created_at=dto.createdAt)
        return property

