from pydispatch import dispatcher
from .handlers import DomainCredentialHandler

#dispatcher.connect(DomainCredentialHandler.handle_credential_created, signal='CredentialCreatedDomain')
#dispatcher.connect(DomainCredentialHandler.handle_credential_created, signal='CredentialCreatedIntegration')
