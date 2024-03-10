from pulsar.schema import *

from src.seedwork.infraestructure.broker_wrapper import BrokerWrapper
from src.seedwork.infraestructure.schema.v1.commands import CommandIntegration, ComandoHandler
from src.seedwork.infraestructure.schema.v1.commands import ejecutar_commando as comando

class CommandStartTransactionPayload(CommandIntegration):
    dni_landlord = String()
    dni_tenant = String()
    id_property = String()
    monetary_value = String()
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


# --------------------------------------------------------------------------------------------------------

class CommandCreateNotificationPayload(CommandIntegration):
    dni_landlord = String()
    dni_tenant = String()
    id_property = String()
    monetary_value = String()
    contract_initial_date = String()
    contract_final_date = String()
    
# --------------------------------------------------------------------------------------------------------

class CommandCreateNotification(CommandIntegration):
    data = CommandCreateNotificationPayload()

class CommandCreateNotificationHandler(ComandoHandler):
    def handle(self, comando: CommandIntegration):
        broker = BrokerWrapper(topic='create-notification-topic', subscription_name='sub-notification', schema=CommandCreateNotification)
        broker.publish(message=comando)

@comando.register(CommandCreateNotification)
def ejecutar_comando_crear_notification(comando: CommandCreateNotification):
    handler = CommandCreateNotificationHandler()
    handler.handle(comando)

# --------------------------------------------------------------------------------------------------------

class CommandReverseNotification(CommandIntegration):
    data = CommandCreateNotificationPayload()

class CommandRemoveNotificationHandler(ComandoHandler):
    def handle(self, comando: CommandIntegration):
        broker = BrokerWrapper(topic='reverse-notification-topic', subscription_name='sub-notification', schema=CommandReverseNotification)
        broker.publish(message=comando)

@comando.register(CommandReverseNotification)
def ejecutar_comando_remover_notification(comando: CommandReverseNotification):
    handler = CommandRemoveNotificationHandler()
    handler.handle(comando)
