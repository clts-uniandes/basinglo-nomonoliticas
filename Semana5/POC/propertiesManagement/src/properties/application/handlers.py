from src.seedwork.application.handlers import Handler
from src.seedwork.application.commands import exec_command
from src.seedwork.application.handlers import Handler
from .commands.save_property import SaveProperty

class DomainPropertyHandler(Handler):
    
    @staticmethod
    def handle_property_created(event):
        print(event)
        command = SaveProperty(
            property_size=event.property_size, 
            total_area_size=event.total_area_size,
            floors_number=event.floors_number,
            is_parking=event.is_parking,
            photos_registry=event.photos_registry,
            ubication=event.ubication,
        )
        exec_command(command)