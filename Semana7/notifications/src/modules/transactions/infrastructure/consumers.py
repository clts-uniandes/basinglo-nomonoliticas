
from src.seedwork.infraestructure.broker_wrapper import BrokerWrapper
from src.modules.transactions.infrastructure.schema.v1.events import EventTransactionCreated, EventTransactionFailed
from src.modules.transactions.infrastructure.schema.v1.commands import CommandCreateTransaction, CommandRemoveTransaction
from src.modules.sagas.application.managers.saga_transaction import ManagerTransaction

def subscribe_to_events():
    transactionCreatedSubscription = BrokerWrapper(topic='created-transaction-topic', subscription_name='sub-transaction', schema=EventTransactionCreated)
    transactionCreatedSubscription.connect()

    transactionFailedSubscription = BrokerWrapper(topic='failed-transaction-topic', subscription_name='sub-transaction', schema=EventTransactionFailed)
    transactionFailedSubscription.connect()
    
    managerTransaction = ManagerTransaction()

    while True:
        message = transactionCreatedSubscription.receive_message()
        print(f'Event received created: {message.value()}')
        managerTransaction.oir_mensaje(message)
        transactionCreatedSubscription.acknowledge_message(message)    

        message2 = transactionFailedSubscription.receive_message()
        print(f'Event received failed: {message2.value()}')
        managerTransaction.oir_mensaje(message2)
        transactionCreatedSubscription.acknowledge_message(message2)    
 

def subscribe_to_commands():
    transactionCreateSubscription = BrokerWrapper(topic='event-create-transaction', subscription_name='sub-transaction', schema=CommandCreateTransaction)
    transactionCreateSubscription.connect()

    transactionRemoveSubscription = BrokerWrapper(topic='event-remove-transaction', subscription_name='sub-transaction', schema=CommandRemoveTransaction)
    transactionRemoveSubscription.connect()

    managerTransaction = ManagerTransaction()

    while True:
        message = transactionCreateSubscription.receive_message()
        print(f'Event received create: {message.value()}')
        managerTransaction.oir_mensaje_command(message)
        transactionCreateSubscription.acknowledge_message(message)     

        message2 = transactionCreateSubscription.receive_message()
        print(f'Event received create: {message2.value()}')
        managerTransaction.oir_mensaje_command(message2)
        transactionCreateSubscription.acknowledge_message(message2)   
