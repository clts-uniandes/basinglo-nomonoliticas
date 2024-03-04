from pulsar.schema import *
from src.seedwork.infraestructure.schema.v1.eventos import EventoIntegracion

class ReservaCreadaPayload(Record):
    #id_reserva = String()
    #id_cliente = String()
    #estado = String()
    #fecha_creacion = Long()
    dni_landlord = String()
    dni_tenant = String()
    monetary_value = Float()
    type_lease = String()
    contract_initial_date = Long()
    contract_final_date = Long

class EventoReservaCreada(EventoIntegracion):
    data = ReservaCreadaPayload()