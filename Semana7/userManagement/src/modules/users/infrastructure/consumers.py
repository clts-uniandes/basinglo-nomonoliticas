import logging
import os
import pulsar
import traceback

from src.modules.users.infrastructure.schema.v1.commands import CommandAddPersonalInfo
from src.modules.users.infrastructure.schema.v1.events import PersonalInfoCreatedEvent
from src.modules.users.application.commands.save_personal_information import SavePersonalInfo
from src.seedwork.application.commands import exec_command

from src.seedwork.infraestructure import utils

PULSAR_TENANT = "PULSAR_TENANT"
PULSAR_NAMESPACE = "PULSAR_NAMESPACE"

USERS_EVENT_TOPIC = "USERS_EVENT_TOPIC"
USERS_COMMAND_TOPIC = "USERS_COMMAND_TOPIC"

USERS_EVENT_SUB_NAME = "USERS_EVENT_SUB_NAME"
USERS_COMMAND_SUB_NAME = "USERS_COMMAND_SUB_NAME"

pulsar_tenant = os.getenv(PULSAR_TENANT, default="public")
pulsar_namespace = os.getenv(PULSAR_NAMESPACE, default="default")

# used
def event_topic_subscribe():
    try:
        event_topic = os.getenv(USERS_EVENT_TOPIC, default="unset")
        subscription_name = os.getenv(USERS_EVENT_SUB_NAME, default="unset")
        client = pulsar.Client(
            f"{utils.broker_url()}",
            authentication=pulsar.AuthenticationToken(utils.broker_token()),
        )
        consumer = client.subscribe(
            pulsar_tenant + "/" + pulsar_namespace + "/" + event_topic,
            consumer_type=pulsar.ConsumerType.Shared,
            subscription_name=subscription_name,
            schema=pulsar.schema.AvroSchema(PersonalInfoCreatedEvent),
        )
        while True:
            message = consumer.receive()
            print(f"Pulsar user event: {message.value()}")
            print(f"Pulsar user event data: {message.value().data}")
            consumer.acknowledge(message)
    except:
        logging.error(
            f'ERROR: Subscription failed!! Full Topic: {pulsar_tenant + "/" + pulsar_namespace + "/" + event_topic}, Subscription: {subscription_name}'
        )
        traceback.print_exc()
        if client:
            client.close()

# not used
def command_event_subscribe():
    try:
        command_topic = os.getenv(USERS_COMMAND_TOPIC, default="unset")
        subscription_name = os.getenv(USERS_COMMAND_SUB_NAME, default="unset")
        client = pulsar.Client(
            f"{utils.broker_url()}",
            authentication=pulsar.AuthenticationToken(utils.broker_token()),
        )
        consumer = client.subscribe(
            pulsar_tenant + "/" + pulsar_namespace + "/" + command_topic,
            consumer_type=pulsar.ConsumerType.Shared,
            subscription_name=subscription_name,
            schema=pulsar.schema.AvroSchema(CommandAddPersonalInfo),
        )
        while True:
            message = consumer.receive()
            payload = message.value().data
            print(f"Pulsar command: {payload}")
            #print(f"Pulsar command: {message.value().data}")
            # this command must be fired from within the domain, NOT outside
            # SavePersonalInfo()
            consumer.acknowledge(message)
    except:
        logging.error(
            f'ERROR: Subscription failed!! Full Topic: {pulsar_tenant + "/" + pulsar_namespace + "/" + event_topic}, Subscription: {subscription_name}'
        )
        traceback.print_exc()
        if client:
            client.close()
