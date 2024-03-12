from src.modules.auth.domain.events import CredentialCreated
from src.modules.users.infrastructure.dispatchers import Dispatcher
from src.seedwork.application.commands import exec_command
from src.seedwork.application.handlers import Handler
from .commands.save_personal_information import SavePersonalInfo


class DomainCredentialHandler(Handler):

    @staticmethod
    def handle_credential_created(event):
        print("----RECEIVED CREATED CREDENTIAL----")
        print(event)
        # data = CredentialCreated(event)
        command = SavePersonalInfo(
            id_credential=event.id_credential,
            email=event.email,
            dni=event.dni,
            fullName=event.fullName,
            phoneNumber=event.phoneNumber,
        )
        exec_command(command)

    #ideally, we would have a different class/file for Integration handlers
    @staticmethod
    def handle_personal_info_created(event):
        print("----GOING TO PULSAR----")
        dispatcher = Dispatcher()
        dispatcher.publish_event(event)
