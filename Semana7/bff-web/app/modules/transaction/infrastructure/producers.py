# import pulsar
from pulsar import Client, AuthenticationToken

from app.seedwork.infrastructure import utils

class Producer:
    def __init__(self): ...

    async def produce_message(self, full_topic, message):
        json_schema = utils.check_schema_registry(full_topic)
        avro_schema = utils.get_avro_schema_from_dict(json_schema)
        # avro_schema = utils.get_avro_schema_from_dict({})
        client = Client(
            f"{utils.broker_url()}",
            authentication=AuthenticationToken(utils.broker_token()),
        )
        print("connection established with: " + utils.broker_url())
        print("target topic: " + "persistent://" + str(full_topic))
        producer = client.create_producer(
            "persistent://" + full_topic, schema=avro_schema
        )
        producer.send(message)
        client.close()
