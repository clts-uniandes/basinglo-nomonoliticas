from pulsar.schema import *

from src.seedwork.infraestructure.schema.v1.commands import CommandIntegration, ComandoHandler
from src.seedwork.infraestructure.schema.v1.commands import ejecutar_commando as comando

class CommandStartTransactionPayload(CommandIntegration):
    dni_landlord = String()
    dni_tenant = String()
    id_property = String()
    monetary_value = String()
    type_lease = String()
    contract_initial_date = String()
    contract_final_date = String()

class CommandStartTransaction(CommandIntegration):
    data = CommandStartTransactionPayload()

class CommandStartTransactionHandler(ComandoHandler):
    def handle(self, comando: CommandIntegration):
        raise NotImplementedError(f'No existe implementación para el comando de tipo {type(comando).__name__}')

@comando.register(CommandStartTransaction)
def ejecutar_comando_crear_transacion(comando: CommandStartTransaction):
    handler = CommandStartTransactionHandler()
    handler.handle(comando)
