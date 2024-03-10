import uuid

from pulsar.schema import Record, String, Long
from src.seedwork.infraestructure.schema.v1.events import IntegrationEvent
from src.seedwork.infraestructure.utils import time_millis


class PersonalInfoCreatedPayload(Record):
    id_credential = String()
    email = String()
    created_at = String()


class PersonalInfoCreatedEvent(IntegrationEvent):
    # REMEMBER: Python Pulsar's Record ignore inherited fields!! Duplicate whatever you need
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = PersonalInfoCreatedPayload()


class PersonalInfoNotCreatedEvent(IntegrationEvent):
    id_credential = String()
    reason = String()
