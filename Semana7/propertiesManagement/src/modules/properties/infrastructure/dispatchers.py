import pulsar
from pulsar.schema import *

from src.seedwork.infraestructure import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Dispatcher:
    def _publicar_mensaje(self, mensaje, topico, schema_avro):
        # cliente = pulsar.Client(f'{utils.broker_host()}', authentication=pulsar.AuthenticationToken(utils.broker_token()))
        # full_topic = f'persistent://${utils.broker_tenant()}/${utils.broker_namespace()}/${topico}'
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=schema_avro)
        #publicador = cliente.create_producer(full_topic, schema=schema_avro)
        publicador.send(mensaje)
        cliente.close()

    def publish_menssage(self, event, topic):        
        self._publicar_mensaje(event, topic, AvroSchema(event.__class__))
