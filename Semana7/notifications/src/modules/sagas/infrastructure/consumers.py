
from src.seedwork.infraestructure.broker_wrapper import BrokerWrapper
from src.modules.transactions.infrastructure.schema.v1.events import EventTransactionCreated, EventTransactionFailed
from src.modules.properties.infrastructure.schema.v1.events import EventPropertyUpdated, EventPropertyUpdatedFailed
from src.modules.sagas.application.managers.saga_transaction import ManagerTransaction
from src.modules.notifications.infrastructure.schema.v1.commands import CommandStartTransaction, CommandCreateNotification, ejecutar_comando_crear_notification
from src.modules.notifications.infrastructure.schema.v1.events import EventNotificationCreated, EventNotificationFailed

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# PASO 0: Iniciar saga con crear
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

def subscribe_to_start_saga_transaction_command():
    transactionStartSubscription = BrokerWrapper(topic='event-start-transaction', subscription_name='sub-notificacion', schema=CommandStartTransaction)
    transactionStartSubscription.connect()
    managerTransaction = ManagerTransaction()
    while True:
        print(f'Event received: {message.value()}')
        message = transactionStartSubscription.receive_message()
        managerTransaction.initializeSteps()
        data = message.value().data
        initCommand = CommandCreateNotification(
            dni_landlord = data.dni_landlord,
            dni_tenant = data.dni_tenant,
            id_property = data.id_property,
            monetary_value = data.monetary_value,
            contract_initial_date = data.contract_initial_date,
            contract_final_date = data.contract_final_date,
        )
        ejecutar_comando_crear_notification(initCommand)
        transactionStartSubscription.acknowledge_message(message)    

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# PASO 1: Crear notificación
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

def subscribe_to_created_notification_event():
    notificationCreatedSubscription = BrokerWrapper(topic='create-notification-topic', subscription_name='sub-transaction', schema=EventNotificationCreated)
    notificationCreatedSubscription.connect()    
    managerTransaction = ManagerTransaction()
    while True:
        message = notificationCreatedSubscription.receive_message()
        print(f'Event received created: {message.value()}')
        managerTransaction.oir_mensaje(message)
        notificationCreatedSubscription.acknowledge_message(message)  


def subscribe_to_failed_notification_event():
    notificationFailedSubscription = BrokerWrapper(topic='create-notification-topic', subscription_name='sub-transaction', schema=EventNotificationFailed)
    notificationFailedSubscription.connect()
    managerTransaction = ManagerTransaction()
    while True:
        message2 = notificationFailedSubscription.receive_message()
        print(f'Event received failed: {message2.value()}')
        managerTransaction.oir_mensaje(message2)
        notificationFailedSubscription.acknowledge_message(message2)    

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# PASO 2: Crear transacción
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

def subscribe_to_created_transaction_event():
    transactionCreatedSubscription = BrokerWrapper(topic='create-transaction-topic', subscription_name='sub-transaction', schema=EventTransactionCreated)
    transactionCreatedSubscription.connect()    
    managerTransaction = ManagerTransaction()
    while True:
        message = transactionCreatedSubscription.receive_message()
        print(f'Event received created: {message.value()}')
        managerTransaction.oir_mensaje(message)
        transactionCreatedSubscription.acknowledge_message(message)    
 

def subscribe_to_failed_transaction_event():
    transactionFailedSubscription = BrokerWrapper(topic='remove-transaction-topic', subscription_name='sub-transaction', schema=EventTransactionFailed)
    transactionFailedSubscription.connect()
    managerTransaction = ManagerTransaction()
    while True:
        message2 = transactionFailedSubscription.receive_message()
        print(f'Event received failed: {message2.value()}')
        managerTransaction.oir_mensaje(message2)
        transactionFailedSubscription.acknowledge_message(message2)    

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# PASO 3: Actualizar propiedad
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

def subscribe_to_updated_property_event():
    propertyUpdatedSubscription = BrokerWrapper(topic='update-property-topic', subscription_name='sub-property', schema=EventPropertyUpdated)
    propertyUpdatedSubscription.connect()
    managerTransaction = ManagerTransaction()
    while True:
        message = propertyUpdatedSubscription.receive_message()
        print(f'Event received created: {message.value()}')
        managerTransaction.oir_mensaje(message)
        propertyUpdatedSubscription.acknowledge_message(message)  


def subscribe_to_failed_updated_property_event():
    propertyFailedSubscription = BrokerWrapper(topic='update-property-topic', subscription_name='sub-property', schema=EventPropertyUpdatedFailed)
    propertyFailedSubscription.connect()
    managerTransaction = ManagerTransaction()
    while True:
        message2 = propertyFailedSubscription.receive_message()
        print(f'Event received failed: {message2.value()}')
        managerTransaction.oir_mensaje(message2)
        propertyFailedSubscription.acknowledge_message(message2) 
