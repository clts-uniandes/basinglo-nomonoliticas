from pulsar.schema import *
from src.seedwork.infraestructure.schema.v1.events import EventIntegracion

class TransactionCreatedPayload(Record):
    id_transaction = String()
    status = String()
    created_at = String()

class EventTransactionCreated(EventIntegracion):
    data = TransactionCreatedPayload()