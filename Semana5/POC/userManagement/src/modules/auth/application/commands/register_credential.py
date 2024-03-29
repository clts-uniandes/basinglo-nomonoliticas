from dataclasses import dataclass

from src.seedwork.application.commands import Command
from src.modules.auth.application.dto import CredentialAppDTO
from .base import RegisterCredentialBaseHandler

from src.seedwork.application.commands import exec_command as command
from src.modules.auth.domain.entities import Credential
from src.seedwork.infraestructure.uow import UnitOfWorkPort
from src.modules.auth.application.mappers import MapperCredential
from src.modules.auth.infrastructure.repositories import CredentialsRepository


@dataclass
class RegisterCredential(Command):
    username: str
    password: str
    email: str
    dni: str
    fullName: str
    phoneNumber: str


class RegisterCredentialHandler(RegisterCredentialBaseHandler):

    def handle(self, command: RegisterCredential):
        credential_dto = CredentialAppDTO(
            username=command.username,
            password=command.password,
            email=command.email,
            dni=command.dni,
            fullName=command.fullName,
            phoneNumber=command.fullName,
            salt=''
        )

        credential: Credential = self.credential_factory.create_object(
            credential_dto, MapperCredential()
        )
        credential.create_credential(credential)

        repository = self.repo_factory.create_object(CredentialsRepository.__class__)

        UnitOfWorkPort.register_batch(repository.add, credential)
        # UnitOfWorkPort.savepoint()
        UnitOfWorkPort.commit()


@command.register(RegisterCredential)
def exec_command_register_credential(command: RegisterCredential):
    handler = RegisterCredentialHandler()
    handler.handle(command)
