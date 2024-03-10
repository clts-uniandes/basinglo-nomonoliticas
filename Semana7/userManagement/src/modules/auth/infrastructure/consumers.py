import logging
import os
import pulsar
import traceback

from src.modules.auth.infrastructure.schema.v1.commands import CommandRegisterCredential
from src.modules.auth.infrastructure.schema.v1.events import CredentialCreatedEvent
from src.modules.auth.application.commands.register_credential import RegisterCredential
from src.seedwork.application.commands import exec_command

from src.seedwork.infraestructure import utils

PULSAR_TENANT = "PULSAR_TENANT"
PULSAR_NAMESPACE = "PULSAR_NAMESPACE"

AUTH_EVENT_TOPIC = "AUTH_EVENT_TOPIC"
AUTH_COMMAND_TOPIC = "AUTH_COMMAND_TOPIC"

AUTH_EVENT_SUB_NAME = "AUTH_EVENT_SUB_NAME"
AUTH_COMMAND_SUB_NAME = "AUTH_COMMAND_SUB_NAME"

pulsar_tenant = os.getenv(PULSAR_TENANT, default="public")
pulsar_namespace = os.getenv(PULSAR_NAMESPACE, default="default")

# not used
def event_topic_subscribe():
    try:
        event_topic = os.getenv(AUTH_EVENT_TOPIC, default="unset")
        subscription_name = os.getenv(AUTH_EVENT_SUB_NAME, default="unset")
        client = pulsar.Client(
            f"{utils.broker_url()}",
            authentication=pulsar.AuthenticationToken(utils.broker_token()),
        )
        consumer = client.subscribe(
            pulsar_tenant + "/" + pulsar_namespace + "/" + event_topic,
            consumer_type=pulsar.ConsumerType.Shared,
            subscription_name=subscription_name,
            schema=pulsar.schema.AvroSchema(CredentialCreatedEvent),
        )
        while True:
            message = consumer.receive()
            print(f"Pulsar auth event: {message.value()}")
            consumer.acknowledge(message)
        # client.close()
    except:
        logging.error(
            f'ERROR: Subscription failed!! Full Topic: {pulsar_tenant + "/" + pulsar_namespace + "/" + event_topic}, Subscription: {subscription_name}'
        )
        traceback.print_exc()
        if client:
            client.close()

# used
def command_event_subscribe():
    try:
        event_topic = os.getenv(AUTH_COMMAND_TOPIC, default="unset")
        subscription_name = os.getenv(AUTH_COMMAND_SUB_NAME, default="unset")
        client = pulsar.Client(
            f"{utils.broker_url()}",
            authentication=pulsar.AuthenticationToken(utils.broker_token()),
        )
        consumer = client.subscribe(
            pulsar_tenant + "/" + pulsar_namespace + "/" + event_topic,
            consumer_type=pulsar.ConsumerType.Shared,
            subscription_name=subscription_name,
            schema=pulsar.schema.AvroSchema(CommandRegisterCredential),
        )
        while True:
            message = consumer.receive()
            payload = message.value().data
            print(f"Pulsar command payload: {payload}")
            #print(f"Pulsar command: {message.value().data}")
            # purpose: to execute the sent command
            
            command = RegisterCredential(
                username=payload.username,
                password=payload.password,
                email=payload.email,
                dni=payload.dni,
                fullName=payload.fullName,
                phoneNumber=payload.phoneNumber,
            )
            exec_command(command)
            consumer.acknowledge(message)
        # client.close()
    except:
        logging.error(
            f'ERROR: Subscription failed!! Full Topic: {pulsar_tenant + "/" + pulsar_namespace + "/" + event_topic}, Subscription: {subscription_name}'
        )
        traceback.print_exc()
        if client:
            client.close()
