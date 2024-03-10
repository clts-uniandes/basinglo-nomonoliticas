import os

from pulsar import Client, AuthenticationToken
from pulsar.schema import AvroSchema

from src.modules.users.infrastructure.schema.v1.commands import CommandAddPersonalInfo, CommandAddPersonalInfoPayload
from src.modules.users.infrastructure.schema.v1.events import PersonalInfoCreatedEvent, PersonalInfoCreatedPayload
from src.seedwork.infraestructure import utils

from src.modules.users.infrastructure.mappers import UserEventsMapper

PULSAR_TENANT = "PULSAR_TENANT"
PULSAR_NAMESPACE = "PULSAR_NAMESPACE"

USERS_EVENT_TOPIC = "USERS_EVENT_TOPIC"
# OTHER_COMMAND_TOPIC = "OTHER_COMMAND_TOPIC"

pulsar_tenant = os.getenv(PULSAR_TENANT, default="public")
pulsar_namespace = os.getenv(PULSAR_NAMESPACE, default="default")

class Dispatcher:
    def __init__(self):
        self.mapper = UserEventsMapper()

    def _publish_message(self, message, topic, schema):
        client = Client(
            utils.broker_url(),
            authentication=AuthenticationToken(utils.broker_token()),
        )
        publisher = client.create_producer(
            "persistent://" + pulsar_tenant+"/"+pulsar_namespace+"/"+topic, schema=AvroSchema(PersonalInfoCreatedEvent)
        )
        publisher.send(message)
        #print("Message published:"+str(message))
        client.close()

    def publish_event(self, event):
        event_topic = os.getenv(USERS_EVENT_TOPIC, default="unset")
        avroEvent = self.mapper.entity_to_dto(event)
        self._publish_message(message=avroEvent, topic=event_topic, schema=AvroSchema(avroEvent.__class__))

    def publish_command(self, command, topic):
        pass
        # shouldn't need an implementation, otherwise tutorial 8
