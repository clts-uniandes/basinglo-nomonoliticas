from src.modules.auth.infrastructure.schema.v1.events import UserCreatedEvent
from src.seedwork.infraestructure import utils
from src.modules.auth.infrastructure.broker_wrapper import BrokerWrapper

def subscribe_to_events():
    UserCreatedEventSubscription = BrokerWrapper(topic='event-credential', subscription_name='sub-notificacion-auth', schema=UserCreatedEvent)
    UserCreatedEventSubscription.connect()

    while True:
        message = UserCreatedEventSubscription.receive_message()
        print(f'Event received: {message.value()}')

        email = message.value().email
        utils.send_email(email)

        UserCreatedEventSubscription.acknowledge_message(message)     
    UserCreatedEventSubscription.close()
