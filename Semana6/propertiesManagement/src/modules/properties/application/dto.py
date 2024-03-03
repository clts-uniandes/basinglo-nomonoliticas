from dataclasses import dataclass, field
from src.seedwork.application.dto import DTO

@dataclass(frozen=True)
class PropertyAppDTO(DTO):
    property_size: float
    property_type: str
    total_area_size: float
    floors_number: int
    is_parking: bool
    photos_registry: str
    ubication: str