from src.seedwork.infraestructure.broker_wrapper import BrokerWrapper
from src.modules.notifications.infrastructure.schema.v1.commands import CommandStartTransaction
from src.modules.sagas.application.managers.saga_transaction import ManagerTransaction

def subscribe_to_commands():
    transactionStartSubscription = BrokerWrapper(topic='event-start-transaction', subscription_name='sub-notificacion', schema=CommandStartTransaction)
    transactionStartSubscription.connect()

    managerTransaction = ManagerTransaction()

    while True:
        print(f'Event received: {message.value()}')
        message = transactionStartSubscription.receive_message()
        managerTransaction.initializeSteps()
        managerTransaction.oir_mensaje_command(message)
        transactionStartSubscription.acknowledge_message(message)     
