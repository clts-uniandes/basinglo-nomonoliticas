from src.modules.auth.domain.events import CredentialCreated
from src.seedwork.application.commands import exec_command
from src.seedwork.application.handlers import Handler
from .commands.save_personal_information import SavePersonalInfo


class DomainCredentialHandler(Handler):

    @staticmethod
    def handle_credential_created(event):
        print("----RECEIVED CREATED CREDENTIAL----")
        print(event)
        #data = CredentialCreated(event)
        command = SavePersonalInfo(
            id_credential=event.id_credential,
            email=event.email,
            dni=event.dni,
            fullName=event.fullName,
            phoneNumber=event.phoneNumber,
        )
        exec_command(command)
        
