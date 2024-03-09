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
            getValor = mensaje.value()
            getProperties = mensaje.properties()
            schema_version = mensaje.schema_version()
            print(f'resultado metodo value: ', getValor)
            print(f'El tipo de dato de value es : ', type(getValor))
            print(f'resultado metodo properties: ', getProperties)
            print(f'El tipo de dato de value es : ', type(getProperties))
            print(f'resultado metodo schema_version: ', schema_version)
            print(f'El tipo de dato de schema_version es : ', type(schema_version))
            print(f'El valor del id del arrendatario es ', getValor.data.dni_landlord)
            print(f'El valor de la compra es  ', getValor.data.monetary_value)
            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()