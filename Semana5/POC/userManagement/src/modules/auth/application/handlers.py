#from src.modules.auth.domain.events import CredentialCreated
from src.seedwork.application.handlers import Handler

class DomainCredentialHandler(Handler):

    @staticmethod
    def handle_credential_created(event):
        print('================ CREDENTIAL CREATED ===========')
        print(event)
        

    