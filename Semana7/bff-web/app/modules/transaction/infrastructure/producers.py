# import pulsar
from pulsar import Client

from . import utils

class Producer:
    def __init__(self):
        ...

    async def produce_message(self, message, topic, schema):
        json_schema = utils.check_schema_registry(schema)  
        avro_schema = utils.get_avro_schema_from_dict(json_schema)
        #avro_schema = utils.get_avro_schema_from_dict({})
        client = Client(f'pulsar://{utils.broker_host()}:6650')
        print("connection established with"+utils.broker_host())
        print("target topic"+str(topic))
        producer = client.create_producer(topic, schema=avro_schema)
        producer.send(message)
        client.close()
        
