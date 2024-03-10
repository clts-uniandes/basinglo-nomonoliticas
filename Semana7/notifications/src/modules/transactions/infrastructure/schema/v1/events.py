from pulsar.schema import *
from src.seedwork.infraestructure.schema.v1.events import EventIntegracion

class TransactionCreatedPayload(Record):
    dni_landlord = String()
    dni_tenant = String()
    id_property = String()
    monetary_value = Float()
    type_lease = String()
    contract_initial_date = Long()
    contract_final_date = Long

class EventTransactionCreated(EventIntegracion):
    data = TransactionCreatedPayload()

class EventTransactionFailed(EventIntegracion):
    data = TransactionCreatedPayload()