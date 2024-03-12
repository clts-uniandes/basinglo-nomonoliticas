from pulsar.schema import String
from src.seedwork.infraestructure.schema.v1.commands import IntegrationCommand


class CommandAddPersonalInfoPayload(IntegrationCommand):
    id_credential = String()
    email = String()
    dni = String()
    fullName = String()
    phoneNumber = String()


class CommandAddPersonalInfo(IntegrationCommand):
    data = CommandAddPersonalInfoPayload()
