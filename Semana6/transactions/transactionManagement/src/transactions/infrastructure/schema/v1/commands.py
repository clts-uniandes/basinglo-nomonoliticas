from pulsar.schema import *
from dataclasses import dataclass, field
from src.seedwork.infraestructure.schema.v1.commands import (CommandIntegration)

class CommandCreateTransactionPayload(CommandIntegration):
    dni_landlord = String()
    dni_tenant = String()
    id_property = String()
    monetary_value = String()
    type_lease = String()
    contract_initial_date = String()
    contract_final_date = String()
    

class CommandCreateTransaction(CommandIntegration):
    data = CommandCreateTransactionPayload()