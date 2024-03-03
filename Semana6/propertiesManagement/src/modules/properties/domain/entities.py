from __future__ import annotations

from dataclasses import dataclass, field
from src.modules.properties.domain.events import PropertyCreated, PropertyUpdated
from src.seedwork.domain.entities import AgregationRoot

@dataclass
class Property(AgregationRoot):
    property_size: float = field(default=None)
    property_type: str = field(default=None)
    total_area_size: float = field(default=None)
    floors_number: int = field(default=None)
    is_parking: bool = field(default=None)
    photos_registry: str = field(default=None)
    ubication: str = field(default=None)

    def create_property(self, property: Property):
        self.property_size = property.property_size
        self.property_type = property.property_type
        self.total_area_size = property.total_area_size
        self.floors_number = property.floors_number
        self.is_parking = property.is_parking
        self.photos_registry = property.photos_registry
        self.ubication = property.ubication

        self.add_event(PropertyCreated(id_property=self.id, created_at=self.created_at))

    def update_property(self, property: Property):
        self.property_size = property.property_size
        self.property_type = property.property_type
        self.total_area_size = property.total_area_size
        self.floors_number = property.floors_number
        self.is_parking = property.is_parking
        self.photos_registry = property.photos_registry
        self.ubication = property.ubication

        self.add_event(PropertyUpdated(id_property=self.id, created_at=self.created_at))
