import pulsar
from pulsar.schema import *

#from aeroalpes.modulos.vuelos.infraestructura.schema.v1.comandos import ComandoCrearReserva, ComandoCrearReservaPayload
from src.seedwork.infraestructure import utils

from src.modules.auth.infrastructure.mappers import EventsCredentialMapper

class Dispatcher:
    def __init__(self):
        self.mapper = EventsCredentialMapper()

    def _publish_menssage(self, message, topic, schema):
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = client.create_producer(topic=topic, schema=schema)
        publicador.send(message)
        client.close()

    def publish_menssage(self, event, topic):
        avroEvent = self.mapper.entity_to_dto(event)
        self._publish_menssage(message=avroEvent, topic=topic, schema=AvroSchema(avroEvent.__class__))

    #def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
    #    payload = ComandoCrearReservaPayload(
    #        id_usuario=str(comando.id_usuario)
            # agregar itinerarios
    #    )
    #    comando_integracion = ComandoCrearReserva(data=payload)
    #    self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearReserva))
