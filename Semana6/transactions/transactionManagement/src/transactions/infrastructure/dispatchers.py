import pulsar
from pulsar.schema import *

from src.transactions.infrastructure.schema.v1.events import EventTransactionCreated, TransactionCreatedPayload, TransactionDeletedPayload, EventTransactionDeleted
from src.transactions.infrastructure.schema.v1.commands import CommandCreateTransaction, CommandCreateTransactionPayload
from src.seedwork.infraestructure import utils

import datetime
import os

epoch = datetime.datetime.utcfromtimestamp(0)

PULSAR_TENANT = "PULSAR_TENANT"
PULSAR_NAMESPACE = "PULSAR_NAMESPACE"

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

pulsar_tenant = os.getenv(PULSAR_TENANT, default="public")
pulsar_namespace = os.getenv(PULSAR_NAMESPACE, default="default")

class Dispatcher:
    def _publicar_mensaje(self, message, topic, schema_avro):
        #cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        client = pulsar.Client(utils.broker_url(), authentication=pulsar.AuthenticationToken(utils.broker_token()),)
        publisher = client.create_producer(
            "persistent://" + pulsar_tenant+"/"+pulsar_namespace+"/"+topic, schema=schema_avro )
        publisher.send(message)
        client.close()
        #publicador = cliente.create_producer(topico, schema=schema_avro)
        #publicador.send(mensaje)
        #cliente.close()


    def publish_command(self, command, topic):        
        payload = CommandCreateTransactionPayload(            
            dni_landlord = str(command.dni_landlord),
            dni_tenant = str(command.dni_tenant),
            id_property = str(command.id_property),            
            monetary_value = float(command.monetary_value),            
            contract_initial_date = str(command.contract_initial_date),
            contract_final_date = (command.contract_final_date)            
        )
        command_integration = CommandCreateTransaction(data=payload)
        self._publicar_mensaje(command_integration, topic, AvroSchema(CommandCreateTransaction))

    def publish_event(self, event, topic):
        payload = TransactionCreatedPayload(
            id_transaction = str(event.id_transaction),
            status = str(event.status),
            created_at = str(event.created_at )
        )
        event_integration = EventTransactionCreated(data=payload)
        self._publicar_mensaje(event_integration, topic, AvroSchema(EventTransactionCreated))


    def publish_event_saga(self, event, topic):
        payload = TransactionDeletedPayload(            
            status = str(event.status)            
        )
        event_integration = EventTransactionDeleted(data=payload)
        self._publicar_mensaje(event_integration, topic, AvroSchema(EventTransactionDeleted))
