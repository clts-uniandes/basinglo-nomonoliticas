import pulsar
from pulsar.schema import *

from src.transactions.infrastructure.schema.v1.eventos import EventoReservaCreada, ReservaCreadaPayload
from src.transactions.infrastructure.schema.v1.comandos import ComandoCrearReserva, ComandoCrearReservaPayload
from src.seedwork.infraestructure import utils
#from aeroalpes.modulos.vuelos.infraestructura.schema.v1.eventos import EventoReservaCreada, ReservaCreadaPayload
#from aeroalpes.modulos.vuelos.infraestructura.schema.v1.comandos import ComandoCrearReserva, ComandoCrearReservaPayload
#from aeroalpes.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(ComandoCrearReserva))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = ReservaCreadaPayload(
            id_reserva=str(evento.id_reserva), 
            id_cliente=str(evento.id_cliente), 
            estado=str(evento.estado), 
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )
        evento_integracion = EventoReservaCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoReservaCreada))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearReservaPayload(            
            #id_usuario=str(comando.id_usuario)
            # agregar itinerarios
            dni_landlord = str(comando.dni_landlord),
            dni_tenant = str(comando.dni_tenant),
            monetary_value = float(comando.monetary_value),
            type_lease = str(comando.type_lease),
            contract_initial_date = int(comando.contract_initial_date),
            contract_final_date = int(comando.contract_final_date)            
        )
        comando_integracion = ComandoCrearReserva(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearReserva))
