from src.config.db import db
from uuid import UUID

from src.transactions.domain.repositories import TransactionRepository
from src.transactions.domain.factories import TransactionFactory
from src.transactions.domain.entities import Transaction
from .mappers import TransactionMapper
from src.transactions.infrastructure.dispatchers import Dispatcher

class TransactionPostgresRepository(TransactionRepository):

    def __init__(self):
        self._transaction_factory: TransactionFactory = (
            TransactionFactory()
        )

    @property
    def credential_factory(self):
        return self._transaction_factory
    
    def get_by_id(self, id: UUID) -> Transaction:
        raise NotImplementedError
    
    def add(self, transaction: Transaction):
        transaction_dto = self._transaction_factory.create_object(
            transaction, TransactionMapper()
        )
        db.session.add(transaction_dto)

    def addAsincronic(self, transaction: Transaction):
        transaction_dto = self._transaction_factory.create_object(
            transaction, TransactionMapper()
        )
        print("Llamamos el despachador desde la capa de infraestructura")
        #db.session.add(transaction_dto)
        command = Dispatcher()
        command.publish_command(transaction_dto, 'topico_prueba_andes')