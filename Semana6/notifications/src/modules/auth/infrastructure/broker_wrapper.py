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
        self.consumer = self.client.subscribe(
            topic=self.topic,
            consumer_type=pulsar.ConsumerType.Shared,
            subscription_name=self.subscription_name,
            schema=AvroSchema(self.schema)
        )

    def receive_message(self):
        msg = self.consumer.receive()
        return msg

    def acknowledge_message(self, msg):
        self.consumer.acknowledge(msg)

    def close(self):
        self.client.close()
