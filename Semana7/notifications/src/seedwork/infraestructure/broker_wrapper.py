import pulsar
from pulsar.schema import AvroSchema
from src.seedwork.infraestructure import utils

class BrokerWrapper:
    def __init__(self, topic, subscription_name, schema):
        self.topic = topic
        self.subscription_name = subscription_name
        self.client = None
        self.consumer = None
        self.schema = schema

    def connect(self):
        self.client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        # self.client = pulsar.Client(f'{utils.broker_host()}', authentication=pulsar.AuthenticationToken(utils.broker_token()))
        # full_topic = f'persistent://${utils.broker_tenant()}/${utils.broker_namespace()}/${self.topic}'

        self.consumer = self.client.subscribe(
            topic=self.topic,
            consumer_type=pulsar.ConsumerType.Shared,
            subscription_name=self.subscription_name,
            schema=AvroSchema(self.schema)
        )

    def publish(self, message):
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        # self.client = pulsar.Client(f'{utils.broker_host()}', authentication=pulsar.AuthenticationToken(utils.broker_token()))
        # full_topic = f'persistent://${utils.broker_tenant()}/${utils.broker_namespace()}/${self.topic}'
        publicador = client.create_producer(
            # topic=full_topic,
            topic=self.topic,
            schema=AvroSchema(self.schema)
        )
        publicador.send(message)
        client.close()

    def receive_message(self):
        msg = self.consumer.receive()
        return msg

    def acknowledge_message(self, msg):
        self.consumer.acknowledge(msg)

    def close(self):
        self.client.close()
