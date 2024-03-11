
import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import os
import time
import logging
import traceback
from src.transactions.infrastructure.schema.v1.commands import CommandCreateTransaction, CommandDeleteTransaction
from src.seedwork.infraestructure import utils
from src.seedwork.infraestructure.projections import execute_projection
from src.transactions.infrastructure.projections import ProjectionReserveConsumer, ProjectionDeleteConsumer


TRANS_COMMAND_SUB_NAME = "TRANS_COMMAND_SUB_NAME"
SAGA_COMMAND_SUB_NAME = "SAGA_COMMAND_SUB_NAME"

PULSAR_TENANT = "PULSAR_TENANT"
PULSAR_NAMESPACE = "PULSAR_NAMESPACE"

pulsar_tenant = os.getenv(PULSAR_TENANT, default="public2")
pulsar_namespace = os.getenv(PULSAR_NAMESPACE, default="default2")

def suscribirse_a_comandos(app=None):
    cliente = None    
    try:
        print(f'Vamos a conectarnos al topico {utils.topic_consumer()}')
        subscription_name = os.getenv(TRANS_COMMAND_SUB_NAME, default="unset")
        print("el nombre de la subscripcion Nelson es ", subscription_name)
        print("El valor de pulsar_tenant es ", pulsar_tenant)
        print("El valor de pulsar namespace es ", pulsar_namespace)
        
        #cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        print("veamos el primero: ")
        print(f'pulsar://{utils.broker_host()}:6650')
        broke_conection=f'{utils.broker_url()}'
        print("veamos el segundo usando la env general : ", broke_conection)        
        cliente = pulsar.Client(broke_conection,authentication=pulsar.AuthenticationToken(utils.broker_token()))

        topico_transaction = f'{utils.topic_consumer()}'  
        print("El nombre del topico Nelson es ", topico_transaction)           
        #consumidor = cliente.subscribe(f'{utils.topic_consumer()}', consumer_type=_pulsar.ConsumerType.Shared, subscription_name=subscription_name, schema=AvroSchema(CommandCreateTransaction))
        consumidor = cliente.subscribe(pulsar_tenant + "/" + pulsar_namespace + "/" + topico_transaction, consumer_type=_pulsar.ConsumerType.Shared, subscription_name=subscription_name, schema=AvroSchema(CommandCreateTransaction))
        
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
            consumidor.acknowledge(mensaje)
            print("Fin de la solicitud del cliente")
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_notificacion_saga(app=None):
    cliente = None    
    try:
        subscription_name = os.getenv(SAGA_COMMAND_SUB_NAME, default="unset")
        print("el nombre de la subscripcion Nelson es ", subscription_name)
        print(f'Vamos a conectarnos al topico de la saga {utils.topic_saga()}')
        broke_conection=f'{utils.broker_url()}'
        cliente = pulsar.Client(broke_conection,authentication=pulsar.AuthenticationToken(utils.broker_token()))
        #cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        topico_transaction_saga = f'{utils.topic_saga()}'
        print("El nombre del topico Nelson es ", topico_transaction_saga)
        #consumidor = cliente.subscribe(f'{utils.topic_saga()}', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='transaction-sub-comandos-saga', schema=AvroSchema(CommandDeleteTransaction))
        consumidor = cliente.subscribe(pulsar_tenant + "/" + pulsar_namespace + "/" + topico_transaction_saga, consumer_type=_pulsar.ConsumerType.Shared, subscription_name=subscription_name, schema=AvroSchema(CommandDeleteTransaction))
        print(f'Cliente conectado al topico {utils.topic_saga()}')

        while True:
            mensaje = consumidor.receive()            
            print(f'Comando recibido: {mensaje.value().data}')
            getValor = mensaje.value()
            print("vamos a ejecutar la proyeccion")
            execute_projection(ProjectionDeleteConsumer(getValor.data.order),app = app)
            print("Vamos a reconocer el mensaje despues de la proyeccion")
            consumidor.acknowledge(mensaje)
            print("Fin de la solicitud del cliente")
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()
