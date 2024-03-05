from src.seedwork.application.commands import CommandHandler
from src.transactions.infrastructure.factories import RepoFactory
from src.transactions.domain.factories import TransactionFactory

class SaveTransactionBaseHandler(CommandHandler):
    def __init__(self):
        self._repo_factory: RepoFactory = RepoFactory()
        self._transaction_factory: TransactionFactory = TransactionFactory()
        
    @property
    def repo_factory(self):
        return self._repo_factory
    
    @property
    def transaction_factory(self):
        return self._transaction_factory