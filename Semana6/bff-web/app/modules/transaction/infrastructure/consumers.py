import aiopulsar
import logging
import pulsar
import traceback
from . import utils

async def topic_subscribe(topic: str, subscription: str, schema: str, consumer_type:pulsar.ConsumerType=pulsar.ConsumerType.Shared, events=[]):
    try:
        json_schema = utils.check_schema_registry(schema)  
        avro_schema = utils.get_avro_schema_from_dict(json_schema)
        async with aiopulsar.connect(f'pulsar://{utils.broker_host()}:6650') as client:
            async with client.subscribe(
                topic, 
                consumer_type=consumer_type,
                subscription_name=subscription, 
                schema=avro_schema
            ) as consumer:
                while True:
                    message = await consumer.receive()
                    print("GOT MESSAGE:"+str(message))
                    payload = message.value()
                    print(f'Payload: {payload}')
                    events.append(str(payload))
                    await consumer.acknowledge(message)    
    except:
        logging.error(f'ERROR: Subscription failed!! Topic: {topic}, Subscription: {subscription}, using schema: {schema}')
        traceback.print_exc()