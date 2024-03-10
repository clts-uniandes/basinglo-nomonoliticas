#from src.modules.auth.domain.events import CredentialCreated
from src.seedwork.application.handlers import Handler
from src.modules.auth.infrastructure.dispatchers import Dispatcher

class DomainCredentialHandler(Handler):

    @staticmethod
    def handle_credential_created(event):
        print('================ CREDENTIAL CREATED ===========')
        print(event)
        #dispatcher = Dispatcher()
        #dispatcher.publish_event(event=event, topic='event-credential')
