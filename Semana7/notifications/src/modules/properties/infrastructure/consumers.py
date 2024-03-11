
from src.seedwork.infraestructure.broker_wrapper import BrokerWrapper
from src.modules.properties.infrastructure.schema.v1.events import EventPropertyUpdated, EventPropertyUpdatedFailed
from src.modules.properties.infrastructure.schema.v1.commands import CommandUpdateProperty
from src.modules.sagas.application.managers.saga_transaction import ManagerTransaction

def subscribe_to_events():
    propertyUpdatedSubscription = BrokerWrapper(topic='event-updated-property', subscription_name='sub-property', schema=EventPropertyUpdated)
    propertyUpdatedSubscription.connect()

    propertyFailedSubscription = BrokerWrapper(topic='event-failed-property', subscription_name='sub-property', schema=EventPropertyUpdatedFailed)
    propertyFailedSubscription.connect()
    
    managerTransaction = ManagerTransaction()

    while True:
        message = propertyUpdatedSubscription.receive_message()
        print(f'Event received created: {message.value()}')
        managerTransaction.oir_mensaje(message)
        propertyUpdatedSubscription.acknowledge_message(message)    

        message2 = propertyFailedSubscription.receive_message()
        print(f'Event received failed: {message2.value()}')
        managerTransaction.oir_mensaje(message2)
        propertyFailedSubscription.acknowledge_message(message2)    
 

def subscribe_to_commands():
    propertyUpdateSubscription = BrokerWrapper(topic='event-update-property', subscription_name='sub-property', schema=CommandUpdateProperty)
    propertyUpdateSubscription.connect()

    managerTransaction = ManagerTransaction()

    while True:
        message = propertyUpdateSubscription.receive_message()
        print(f'Event received update: {message.value()}')
        managerTransaction.oir_mensaje_command(message)
        propertyUpdateSubscription.acknowledge_message(message)     
