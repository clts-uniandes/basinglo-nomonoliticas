from pulsar.schema import *
from src.seedwork.infraestructure.broker_wrapper import BrokerWrapper
from src.seedwork.infraestructure.schema.v1.commands import CommandIntegration
from src.seedwork.infraestructure.schema.v1.commands import CommandIntegration, ComandoHandler
from src.seedwork.infraestructure.schema.v1.commands import ejecutar_commando as comando

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

class CommandUpdatePropertyHandler(ComandoHandler):
    def handle(self, comando: CommandIntegration):
        broker = BrokerWrapper(topic='event-update-property', subscription_name='sub-property', schema=CommandUpdateProperty)
        broker.publish(message=comando)

@comando.register(CommandUpdateProperty)
def ejecutar_comando_actualizar_propiedad(comando: CommandUpdateProperty):
    handler = CommandUpdatePropertyHandler()
    handler.handle(comando)
