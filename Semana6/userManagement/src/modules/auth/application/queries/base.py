from src.seedwork.application.queries import QueryHandler
from src.modules.auth.infrastructure.factories import RepoFactory
from src.modules.auth.domain.factories import CredentialFactory

class CredentialQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._repo_factory: RepoFactory = RepoFactory()
        self._credentials_factory: CredentialFactory = CredentialFactory()

    @property
    def repo_factory(self):
        return self._repo_factory
    
    @property
    def credential_factory(self):
        return self._credentials_factory    
