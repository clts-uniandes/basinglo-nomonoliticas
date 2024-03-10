from pydispatch import dispatcher
from .handlers import DomainCredentialHandler

# "local"
dispatcher.connect(DomainCredentialHandler.handle_credential_created, signal='CredentialCreatedDomain')
# requires pulsar
dispatcher.connect(DomainCredentialHandler.handle_personal_info_created, signal='PersonalInfoCreatedIntegration')
