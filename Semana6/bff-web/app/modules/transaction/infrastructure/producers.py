# import pulsar
from pulsar import Client

from . import utils

class Producer:
    def __init__(self):
        ...

    async def publish_message(self, message, topic, schema):
        json_schema = utils.check_schema_registry(schema)  
        avro_schema = utils.get_avro_schema_from_dict(json_schema)

        client = Client(f'pulsar://{utils.broker_host()}:6650')
        publisher = client.create_producer(topic, schema=avro_schema)
        publisher.send(message)
        client.close() 
