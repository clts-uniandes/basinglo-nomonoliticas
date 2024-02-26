from dataclasses import dataclass

from src.seedwork.application.queries import Query, QueryResult, exec_query as query
from src.modules.auth.infrastructure.repositories import CredentialsRepository
from src.modules.auth.domain.entities import Credential
from .base import CredentialQueryBaseHandler
from src.modules.auth.application.mappers import MapperCredential
from src.modules.auth.infrastructure.utils import verify_password

@dataclass
class AuthenticateUser(Query):
    username: str
    password: str

class AuthenticateUserHandler(CredentialQueryBaseHandler):

    def handle(self, query: AuthenticateUser) -> QueryResult:
        repository = self.repo_factory.create_object(CredentialsRepository.__class__)
        credential = self.credential_factory.create_object(repository.get_by_username(query.username), MapperCredential())
        verified_password = verify_password(hashed_password=credential.password, salt=credential.salt, password_to_check=query.password)
        if not verified_password:
            raise Exception("Invalid credentials")
        
        return QueryResult(result=credential)

@query.register(AuthenticateUser)
def exec_query_authenticate_user(query: AuthenticateUser):
    handler = AuthenticateUserHandler()
    return handler.handle(query)
