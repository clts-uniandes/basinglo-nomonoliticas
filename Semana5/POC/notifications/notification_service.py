import pulsar
from os import environ as env
from pulsar.schema import *

HOSTNAME = env.get('BROKER_PATH', default="broker")
PULSAR_TOPIC = 'user_created'

class UserCreatedEvent(Record):
    email = String()

client = pulsar.Client(f'pulsar://{HOSTNAME}:6650')
consumer = client.subscribe(topic=PULSAR_TOPIC, subscription_name='sub-notificacion-auth', schema=AvroSchema(UserCreatedEvent))

while True:
    msg = consumer.receive()
    data = msg.value()
    try:
        print("Received message email={}".format(data.email))
    except Exception as e:
        print("Error processing event:", str(e))
    consumer.acknowledge(msg)
