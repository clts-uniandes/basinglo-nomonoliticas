import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from src.transactions.infrastructure.schema.v1.commands import CommandCreateTransactionPayload, CommandCreateTransaction
from src.seedwork.infraestructure import utils

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe(f'{utils.topic_consumer()}', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='transaction-sub-comandos', schema=AvroSchema(CommandCreateTransaction))
        print(f'Cliente conectado al topico {utils.topic_consumer()}')

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()