
import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import os
import logging
import traceback
from src.transactions.infrastructure.schema.v1.commands import CommandCreateTransaction, CommandDeleteTransaction
from src.seedwork.infraestructure import utils
from src.seedwork.infraestructure.projections import execute_projection
from src.transactions.infrastructure.projections import ProjectionReserveConsumer, ProjectionDeleteConsumer

PULSAR_TENANT = "PULSAR_TENANT"
PULSAR_NAMESPACE = "PULSAR_NAMESPACE"

TRANS_EVENT_TOPIC = "TRANS_EVENT_TOPIC"
TRANS_COMMAND_TOPIC = "TRANS_COMMAND_TOPIC"

TRANS_COMMAND_SUB_NAME = "TRANS_COMMAND_SUB_NAME"
TRANS_EVENT_SUB_NAME = "TRANS_EVENT_SUB_NAME"

pulsar_tenant = os.getenv(PULSAR_TENANT, default="public")
pulsar_namespace = os.getenv(PULSAR_NAMESPACE, default="default")

def suscribirse_a_comandos(app=None):
    client = None    
    try:
        
        #print(f'Vamos a conectarnos al topico {utils.topic_consumer()}')
        command_topic = os.getenv(TRANS_COMMAND_TOPIC, default="unset")
        subscription_name = os.getenv(TRANS_COMMAND_SUB_NAME, default="unset")
        client = pulsar.Client(
            f"{utils.broker_url()}",
            authentication=pulsar.AuthenticationToken(utils.broker_token()),
        )
        
        consumer = client.subscribe(
            pulsar_tenant + "/" + pulsar_namespace + "/" + command_topic,
            consumer_type=pulsar.ConsumerType.Shared,
            subscription_name=subscription_name,
            schema=pulsar.schema.AvroSchema(CommandCreateTransaction),
        )
        
        #cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')        
        #consumidor = cliente.subscribe(f'{utils.topic_consumer()}', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='transaction-sub-comandos', schema=AvroSchema(CommandCreateTransaction))
        print(f'Cliente conectado al topico {utils.topic_consumer()}')

        while True:
            mensaje = consumer.receive()            
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
            #print(f'El valor del id del arrendatario es ', getValor.data.dni_landlord)
            #print(f'El valor de la compra es  ', getValor.data.monetary_value)
            print("vamos a ejecutar la proyeccion")
            execute_projection(ProjectionReserveConsumer(getValor.data.dni_landlord,
                                                         getValor.data.dni_tenant,
                                                         getValor.data.id_property,
                                                         getValor.data.monetary_value,
                                                         getValor.data.contract_initial_date,
                                                         getValor.data.contract_final_date
                                                         ),app = app)            
            
            print("Vamos a reconocer el mensaje despues de la proyeccion")
            consumer.acknowledge(mensaje)
            print("Fin de la solicitud del cliente")
        client.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if client:
            client.close()


def suscribirse_a_notificacion_saga(app=None):
    client = None    
    try:
        #print(f'Vamos a conectarnos al topico de la saga {utils.topic_saga()}')
        
        event_topic = os.getenv(TRANS_EVENT_TOPIC, default="unset")
        subscription_name = os.getenv(TRANS_EVENT_SUB_NAME, default="unset")
        client = pulsar.Client(
            f"{utils.broker_url()}",
            authentication=pulsar.AuthenticationToken(utils.broker_token()),
        )
        consumer = client.subscribe(
            pulsar_tenant + "/" + pulsar_namespace + "/" + event_topic,
            consumer_type=pulsar.ConsumerType.Shared,
            subscription_name=subscription_name,
            schema=pulsar.schema.AvroSchema(CommandDeleteTransaction),
        )
        
        #cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')        
        #consumidor = cliente.subscribe(f'{utils.topic_saga()}', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='transaction-sub-comandos-saga', schema=AvroSchema(CommandDeleteTransaction))
        #print(f'Cliente conectado al topico {utils.topic_saga()}')

        while True:
            mensaje = consumer.receive()            
            print(f'Comando recibido: {mensaje.value().data}')
            getValor = mensaje.value()
            print("vamos a ejecutar la proyeccion")
            execute_projection(ProjectionDeleteConsumer(getValor.data.order),app = app)
            print("Vamos a reconocer el mensaje despues de la proyeccion")
            consumer.acknowledge(mensaje)
            print("Fin de la solicitud del cliente")
        client.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if client:
            client.close()
