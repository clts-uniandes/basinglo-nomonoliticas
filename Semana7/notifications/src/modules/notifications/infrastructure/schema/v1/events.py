import time as timelib
import uuid
from pulsar.schema import *
from src.seedwork.infraestructure.schema.v1.events import EventIntegracion

class EventNotificationCreatedPayload(Record):
    dni_landlord = String()
    dni_tenant = String()
    id_property = String()
    monetary_value = Float()
    contract_initial_date = Long()
    contract_final_date = Long()

class EventNotificationCreated(EventIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=int(timelib.time() * 1000))
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = EventNotificationCreatedPayload()

class EventNotificationFailed(EventIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=int(timelib.time() * 1000))
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = EventNotificationCreatedPayload()