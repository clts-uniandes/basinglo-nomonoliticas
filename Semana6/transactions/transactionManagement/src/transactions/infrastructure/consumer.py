import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from src.transactions.application.commands.save_transaction import SaveTransaction
from src.seedwork.application.commands import exec_command

from src.transactions.infrastructure.schema.v1.commands import CommandCreateTransactionPayload, CommandCreateTransaction
from src.seedwork.infraestructure import utils
import requests

def suscribirse_a_comandos():
    cliente = None    
    try:
        print(f'Vamos a conectarnos al topico {utils.topic_consumer()}')
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
            #print(f'El valor del id del arrendatario es ', getValor.data.dni_landlord)
            #print(f'El valor de la compra es  ', getValor.data.monetary_value)
            '''
            command = SaveTransaction(dni_landlord=getValor.data.dni_landlord,
                               dni_tenant=getValor.data.dni_tenant,
                               id_property=getValor.data.id_property,
                               monetary_value=getValor.data.monetary_value,                               
                               contract_initial_date=getValor.data.contract_initial_date,
                               contract_final_date=getValor.data.contract_final_date)
            exec_command(command)
            '''
            data = {"dni_landlord":getValor.data.dni_landlord,
                    "dni_tenant":getValor.data.dni_tenant,
                    "id_property":getValor.data.id_property,
                    "monetary_value":getValor.data.monetary_value,
                    "contract_initial_date":getValor.data.contract_initial_date,
                    "contract_final_date":getValor.data.contract_final_date
                    }
            #url = "http://localhost:8000/transactions/add"
            url = "http://localhost:8000/transactions/addCommand"
            response = requests.post(url, json=data)
            print("Status Code", response.status_code)
            consumidor.acknowledge(mensaje)
            print("Fin de la solicitud del cliente")
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

