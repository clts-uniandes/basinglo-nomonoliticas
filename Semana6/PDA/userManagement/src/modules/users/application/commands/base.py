from src.seedwork.application.commands import CommandHandler
from src.modules.users.infrastructure.factories import RepoFactory
from src.modules.users.domain.factories import PersonalInformationFactory

class SavePersonalInformationBaseHandler(CommandHandler):
    def __init__(self):
        self._repo_factory: RepoFactory = RepoFactory()
        self._personal_info_factory: PersonalInformationFactory = PersonalInformationFactory()

    @property
    def repo_factory(self):
        return self._repo_factory
    
    @property
    def personal_info_factory(self):
        return self._personal_info_factory    
