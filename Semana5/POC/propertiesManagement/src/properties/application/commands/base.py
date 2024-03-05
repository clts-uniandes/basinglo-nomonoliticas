from src.seedwork.application.commands import CommandHandler
from src.properties.infrastructure.factories import RepoFactory
from src.properties.domain.factories import PropertyFactory

class SavePropertyBaseHandler(CommandHandler):
    def __init__(self):
        self._repo_factory: RepoFactory = RepoFactory()
        self._personal_info_factory: PropertyFactory = PropertyFactory()
        
    @property
    def repo_factory(self):
        return self._repo_factory
    
    @property
    def property_factory(self):
        return self._property_factory