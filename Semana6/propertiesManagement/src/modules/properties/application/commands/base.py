from src.seedwork.application.commands import CommandHandler
from src.modules.properties.infrastructure.factories import RepoFactory
from src.modules.properties.domain.factories import PropertyFactory

class SavePropertyBaseHandler(CommandHandler):
    def __init__(self):
        self._repo_factory: RepoFactory = RepoFactory()
        self._property_factory: PropertyFactory = PropertyFactory()
        
    @property
    def repo_factory(self):
        return self._repo_factory
    
    @property
    def property_factory(self):
        return self._property_factory

class UpdatePropertyBaseHandler(CommandHandler):
    def __init__(self):
        self._repo_factory: RepoFactory = RepoFactory()
        self._property_factory: PropertyFactory = PropertyFactory()
        
    @property
    def repo_factory(self):
        return self._repo_factory
    
    @property
    def property_factory(self):
        return self._property_factory