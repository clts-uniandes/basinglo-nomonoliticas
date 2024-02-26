from src.seedwork.application.commands import CommandHandler
from src.modules.auth.infrastructure.factories import RepoFactory
from src.modules.auth.domain.factories import CredentialFactory

class RegisterCredentialBaseHandler(CommandHandler):
    def __init__(self):
        self._repo_factory: RepoFactory = RepoFactory()
        self._credential_factory: CredentialFactory = CredentialFactory()

    @property
    def repo_factory(self):
        return self._repo_factory
    
    @property
    def credential_factory(self):
        return self._credential_factory
