from src.config.db import db
from uuid import UUID

from src.transactions.domain.repositories import TransactionRepository
from src.transactions.domain.factories import TransactionFactory
from src.transactions.domain.entities import Transaction
from .mappers import TransactionMapper
from src.transactions.infrastructure.dispatchers import Dispatcher
from src.seedwork.infraestructure import utils

import threading
import src.transactions.infrastructure.consumer as consumer

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
        db.session.add(transaction_dto)
        #threading.Thread(target=consumer.suscribirse_a_comandos).start()
        command = Dispatcher()
        topic = f'{utils.topic()}'       
        print("El valor del topic es ", topic)
        command.publish_command(transaction_dto, topic)