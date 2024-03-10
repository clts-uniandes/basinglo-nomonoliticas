from pulsar.schema import String
from src.seedwork.infraestructure.schema.v1.commands import IntegrationCommand


class CommandRegisterCredentialPayload(IntegrationCommand):
    username = String()
    password = String()
    email = String()
    dni = String()
    fullName = String()
    phoneNumber = String()


class CommandRegisterCredential(IntegrationCommand):
    data = CommandRegisterCredentialPayload()
