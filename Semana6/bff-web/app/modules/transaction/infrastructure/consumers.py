import aiopulsar
import logging
import pulsar
import traceback
from . import utils

async def topic_subscribe(topic: str, subscription: str, full_topic: str, consumer_type:pulsar.ConsumerType=pulsar.ConsumerType.Shared, events=[]):
    # schema route debe tener la forma tenant/namespace/topic
    try:
        json_schema = utils.check_schema_registry(full_topic)  
        avro_schema = utils.get_avro_schema_from_dict(json_schema)
        #avro_schema = utils.get_avro_schema_from_dict({})
        async with aiopulsar.connect(f'pulsar://{utils.broker_host()}:6650') as client:
            async with client.subscribe(
                topic=topic, 
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
        logging.error(f'ERROR: Subscription failed!! Full Topic: {full_topic}, Subscription: {subscription}, using schema: {str(avro_schema)}')
        traceback.print_exc()