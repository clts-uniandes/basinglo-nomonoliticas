from pulsar.schema import *
from src.seedwork.infraestructure.schema.v1.events import EventIntegracion

class NotificationCreatedPayload(Record):
    dni_landlord = String()
    dni_tenant = String()
    id_property = String()
    monetary_value = Float()
    contract_initial_date = Long()
    contract_final_date = Long

class EventNotificationCreated(EventIntegracion):
    data = NotificationCreatedPayload()

class EventNotificationFailed(EventIntegracion):
    data = NotificationCreatedPayload()