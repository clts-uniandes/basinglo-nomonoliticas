from src.transactions.application.dto import TransactionAppDTO
from src.seedwork.infraestructure.projections import Projection, ProjectionHandler
from src.seedwork.infraestructure.projections import execute_projection as projection
from src.transactions.infrastructure.factories import RepoFactory
from src.transactions.infrastructure.repositories import TransactionRepository
from src.transactions.domain.factories import TransactionFactory
from src.transactions.domain.entities import Transaction
from src.transactions.application.mappers import MapperTransaction
import logging
import traceback
from abc import ABC, abstractmethod


class ProjectionReserve(Projection,ABC):
    @abstractmethod
    def execute(self):
        ...


class ProjectionReserveConsumer(ProjectionReserve):
    def __init__(self,dni_landlord,dni_tenant,id_property,monetary_value,contract_initial_date,contract_final_date):
        self.dni_landlord = dni_landlord
        self.dni_tenant = dni_tenant
        self.id_property = id_property
        self.monetary_value = monetary_value
        self.contract_initial_date = contract_initial_date
        self.contract_final_date = contract_final_date

    def execute(self, db= None):
        if not db:
            logging.error('ERROR: DB del app no puede ser nula')
            return       

        transaction_dto = TransactionAppDTO(
            self.dni_landlord,
            self.dni_tenant,
            self.id_property,
            self.monetary_value,           
            self.contract_initial_date,
            self.contract_final_date           
        )
        self.transaction_factory: TransactionFactory = TransactionFactory()
        self.repo_factory: RepoFactory = RepoFactory()        
        transaction: Transaction = self.transaction_factory.create_object(
            transaction_dto, MapperTransaction())
        transaction.create_transaction(transaction)
        repository = self.repo_factory.create_object(
            TransactionRepository.__class__
        )
        repository.addAsincronic(transaction)

        db.session.commit()

class ProjectionReserveHandler(ProjectionHandler):    
    def handle(self, projection: ProjectionReserve):
        from src.config.db import db
        projection.execute(db=db)


@projection.register(ProjectionReserveConsumer)
def execute_projection_reserve(projection, app=None):
    
    try:        
        handler = ProjectionReserveHandler()
        handler.handle(projection)
            
    except:
        traceback.print_exc()
        logging.error('ERROR: Persistiendo!')


####### DELETE Transaction ######

class ProjectionDelete(Projection,ABC):
    @abstractmethod
    def execute(self):
        ...


class ProjectionDeleteConsumer(ProjectionDelete):
    def __init__(self,order):
        self.order = order        

    def execute(self, db= None):
        if not db:
            logging.error('ERROR: DB del app no puede ser nula')
            return
        
        self.repo_factory: RepoFactory = RepoFactory()
        repository = self.repo_factory.create_object(
            TransactionRepository.__class__
        )
        repository.deleteAsincronic()
        db.session.commit()


class ProjectionDeleteHandler(ProjectionHandler):    
    def handle(self, projection: ProjectionDelete):
        from src.config.db import db
        projection.execute(db=db)


@projection.register(ProjectionDeleteConsumer)
def execute_projection_delete(projection, app=None):
    
    try:        
        handler = ProjectionDeleteHandler()
        handler.handle(projection)
            
    except:
        traceback.print_exc()
        logging.error('ERROR: Eliminando!')


