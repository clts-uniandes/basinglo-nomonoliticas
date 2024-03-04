from pulsar.schema import *
from dataclasses import dataclass, field
from src.seedwork.infraestructure.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearReservaPayload(ComandoIntegracion):
    #id_usuario = String()
    # TODO Cree los records para itinerarios
    dni_landlord = String()
    dni_tenant = String()
    monetary_value = Float()
    type_lease = String()
    contract_initial_date = Long()
    contract_final_date = Long
    

class ComandoCrearReserva(ComandoIntegracion):
    data = ComandoCrearReservaPayload()