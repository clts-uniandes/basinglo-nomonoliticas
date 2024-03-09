import pulsar
from pulsar.schema import *

from src.transactions.infrastructure.schema.v1.events import EventTransactionCreated, TransactionCreatedPayload
from src.transactions.infrastructure.schema.v1.commands import CommandCreateTransaction, CommandCreateTransactionPayload
from src.seedwork.infraestructure import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Dispatcher:
    def _publicar_mensaje(self, mensaje, topico, schema_avro):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=schema_avro)
        publicador.send(mensaje)
        cliente.close()


    def publish_command(self, command, topic):        
        payload = CommandCreateTransactionPayload(            
            dni_landlord = str(command.dni_landlord),
            dni_tenant = str(command.dni_tenant),
            id_property = str(command.id_property),
            #monetary_value = str(command.monetary_value),
            monetary_value = float(command.monetary_value),            
            contract_initial_date = str(command.contract_initial_date),
            contract_final_date = (command.contract_final_date)            
        )
        command_integration = CommandCreateTransaction(data=payload)
        self._publicar_mensaje(command_integration, topic, AvroSchema(CommandCreateTransaction))
