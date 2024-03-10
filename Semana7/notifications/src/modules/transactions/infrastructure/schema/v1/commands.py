from pulsar.schema import *
from src.seedwork.infraestructure.broker_wrapper import BrokerWrapper
from src.seedwork.infraestructure.schema.v1.commands import CommandIntegration, ComandoHandler
from src.seedwork.infraestructure.schema.v1.commands import ejecutar_commando as comando

class CommandCreateTransactionPayload(CommandIntegration):
    dni_landlord = String()
    dni_tenant = String()
    id_property = String()
    monetary_value = String()
    contract_initial_date = String()
    contract_final_date = String()
    
# --------------------------------------------------------------------------------------------------------


class CommandCreateTransaction(CommandIntegration):
    data = CommandCreateTransactionPayload()

class CommandCreateTransactionHandler(ComandoHandler):
    def handle(self, comando: CommandIntegration):
        broker = BrokerWrapper(topic='create-transaction-topic', subscription_name='sub-transaction', schema=CommandCreateTransaction)
        broker.publish(message=comando)

@comando.register(CommandCreateTransaction)
def ejecutar_comando_crear_transacion(comando: CommandCreateTransaction):
    handler = CommandCreateTransactionHandler()
    handler.handle(comando)

# --------------------------------------------------------------------------------------------------------

class CommandRemoveTransaction(CommandIntegration):
    data = CommandCreateTransactionPayload()

class CommandRemoveTransactionHandler(ComandoHandler):
    def handle(self, comando: CommandIntegration):
        broker = BrokerWrapper(topic='remove-transaction-topic', subscription_name='sub-transaction', schema=CommandRemoveTransaction)
        broker.publish(message=comando)

@comando.register(CommandRemoveTransaction)
def ejecutar_comando_remover_transacion(comando: CommandRemoveTransaction):
    handler = CommandRemoveTransactionHandler()
    handler.handle(comando)
