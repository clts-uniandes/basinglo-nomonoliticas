import os

from pulsar import Client, AuthenticationToken
from pulsar.schema import AvroSchema

from src.modules.auth.infrastructure.schema.v1.commands import CommandRegisterCredential, CommandRegisterCredentialPayload
from src.modules.auth.infrastructure.schema.v1.events import CredentialCreatedEvent, CredentialCreatedPayload
from src.seedwork.infraestructure import utils

from src.modules.auth.infrastructure.mappers import CredentialEventsMapper

PULSAR_TENANT = "PULSAR_TENANT"
PULSAR_NAMESPACE = "PULSAR_NAMESPACE"

AUTH_EVENT_TOPIC = "AUTH_EVENT_TOPIC"
# OTHER_COMMAND_TOPIC = "OTHER_COMMAND_TOPIC"

pulsar_tenant = os.getenv(PULSAR_TENANT, default="public")
pulsar_namespace = os.getenv(PULSAR_NAMESPACE, default="default")

class Dispatcher:
    def __init__(self):
        self.mapper = CredentialEventsMapper()

    def _publish_message(self, message, topic, schema):
        client = Client(
            utils.broker_url(),
            authentication=AuthenticationToken(utils.broker_token()),
        )
        publisher = client.create_producer(
            "persistent://" + pulsar_tenant+"/"+pulsar_namespace+"/"+topic, schema=AvroSchema(CredentialCreatedEvent)
        )
        publisher.send(message)
        client.close()

    def publish_event(self, event):
        event_topic = os.getenv(AUTH_EVENT_TOPIC, default="unset")
        avroEvent = self.mapper.entity_to_dto(event)
        self._publish_message(message=avroEvent, topic=event_topic, schema=AvroSchema(avroEvent.__class__))

    def publish_command(self, command, topic):
        pass
        # shouldn't need an implementation, otherwise tutorial 8
