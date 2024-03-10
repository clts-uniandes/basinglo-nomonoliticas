
from src.seedwork.infraestructure.broker_wrapper import BrokerWrapper
from src.modules.notifications.infrastructure.schema.v1.events import EventNotificationCreated, EventNotificationFailed
from src.modules.notifications.infrastructure.schema.v1.commands import CommandCreateNotification, CommandReverseNotification
from src.modules.sagas.seedwork.infraestructure.utils import send_email

def subscribe_to_create_notification_command():
    notificationCreateSubscription = BrokerWrapper(topic='create-notification-topic', subscription_name='sub-notification', schema=CommandCreateNotification)
    notificationCreateSubscription.connect()

    while True:
        message = notificationCreateSubscription.receive_message()
        print(f'Event received create: {message.value()}')
        transaction_data = message.value().data

        try:
            send_email(f'This is a notification for {transaction_data.dni_tenant} transaction, lets start with saga')
            notification_created_event = EventNotificationCreated(
                dni_landlord = transaction_data.dni_landlord,
                dni_tenant = transaction_data.dni_tenant,
                id_property = transaction_data.id_property,
                monetary_value = transaction_data.monetary_value,
                contract_initial_date = transaction_data.contract_initial_date,
                contract_final_date = transaction_data.contract_final_date,
            )
            notificationCreateSubscription.publish(notification_created_event) # check if we need to use another topic
        except Exception as e:
            notification_created_event = EventNotificationFailed(
                dni_landlord = transaction_data.dni_landlord,
                dni_tenant = transaction_data.dni_tenant,
                id_property = transaction_data.id_property,
                monetary_value = transaction_data.monetary_value,
                contract_initial_date = transaction_data.contract_initial_date,
                contract_final_date = transaction_data.contract_final_date,
            )
            notificationCreateSubscription.publish(notification_created_event)

        notificationCreateSubscription.acknowledge_message(message)     



def subscribe_to_reverse_notification_command():
    notificationReverseSubscription = BrokerWrapper(topic='reverse-notification-topic', subscription_name='sub-notification', schema=CommandReverseNotification)
    notificationReverseSubscription.connect()
    while True:
        message = notificationReverseSubscription.receive_message()
        print(f'Event received create: {message.value()}')
        transaction_data = message.value().data
        send_email(f'This is a notification to reverse {transaction_data.dni_tenant} transaction')
        notificationReverseSubscription.acknowledge_message(message)     
