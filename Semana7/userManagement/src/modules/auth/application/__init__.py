from pydispatch import dispatcher
from .handlers import DomainCredentialHandler

# we don't integrate with others, and we only care about full credentials AND personal data, so disabled for now
#dispatcher.connect(DomainCredentialHandler.handle_credential_created, signal='CredentialCreatedDomain')
#dispatcher.connect(DomainCredentialHandler.handle_credential_created, signal='CredentialCreatedIntegration')
