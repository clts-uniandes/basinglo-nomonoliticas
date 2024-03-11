from src.config.db import db
from uuid import UUID

from src.transactions.domain.repositories import TransactionRepository
from src.transactions.domain.factories import TransactionFactory
from src.transactions.domain.entities import ResponseTransaction, Transaction, ResponseSaga
from .mappers import TransactionMapper
from src.transactions.infrastructure.dispatchers import Dispatcher
from src.seedwork.infraestructure import utils

import threading
import src.transactions.infrastructure.consumer as consumer
from .dto import Transaction as TransactionDTO
import logging
import traceback

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

        enable_transaction = {utils.enable_transaction}
        event = Dispatcher()
        topic = f'{utils.topic()}'       
        print("El valor del topic es ", topic)
        print("El valor del enable es ", enable_transaction)  
        if enable_transaction == True:
            print("Llamamos el despachador desde la capa de infraestructura")
            db.session.add(transaction_dto)
            last_record = db.session.query(TransactionDTO).filter_by(id_property = transaction_dto.id_property).first()
            print("Los elementos de la base de datos es {} y  propiedad Id es {}".format(last_record.id,last_record.id_property))
            response = ResponseTransaction(id_transaction=last_record.id, status="Transaction OK", created_at=last_record.createdAt)
            event.publish_event(response, topic)
        else:
            print("publicamos mensaje de transaccion falida")
            response = ResponseTransaction(id_transaction="", status="Transaction Fail", created_at="")
            event.publish_event(response, topic)

    def deleteAsincronic(self):
        try:
            transaction = db.session.query(TransactionDTO).first()
            db.session.delete(transaction)
            event = Dispatcher()
            topic = f'{utils.topic_saga_response()}'
            print("El valor del topic es ", topic)
            response = ResponseSaga(status="Compensacion exitosa!!!")
            event.publish_event_saga(response, topic)

        except:
            traceback.print_exc()
            logging.error('ERROR: No hay datos en la BD!')


