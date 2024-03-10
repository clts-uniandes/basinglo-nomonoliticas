import aiopulsar
import logging
import pulsar
import traceback
from app.seedwork.infrastructure import utils


async def topic_subscribe(
    full_topic: str,
    subscription: str,
    consumer_type: pulsar.ConsumerType = pulsar.ConsumerType.Shared,
    events=[],
):
    # servicios nube no permiten y/o no crean por defecto public/default
    # full_topic debe tener la forma tenant/namespace/topic
    try:
        avro_schema = "Not Ready"
        json_schema = utils.check_schema_registry(full_topic)
        avro_schema = utils.get_avro_schema_from_dict(json_schema)
        # avro_schema = utils.get_avro_schema_from_dict({})
        async with aiopulsar.connect(
            f"{utils.broker_url()}",
            authentication=pulsar.AuthenticationToken(utils.broker_token()),
        ) as client:
            async with client.subscribe(
                topic="persistent://" + full_topic,
                consumer_type=consumer_type,
                subscription_name=subscription,
                schema=avro_schema,
            ) as consumer:
                while True:
                    message = await consumer.receive()
                    payload = message.value()
                    print(f"GOT MESSAGE! Payload: {payload}")
                    events.append(str(payload))
                    await consumer.acknowledge(message)
    except:
        logging.error(
            f"ERROR: Subscription failed!! Full Topic: {full_topic}, Subscription: {subscription}, using schema: {str(avro_schema)}"
        )
        traceback.print_exc()
