from dataclasses import dataclass
from datetime import date

from src.seedwork.application.commands import Command
from src.transactions.application.dto import TransactionAppDTO
from .base import SaveTransactionBaseHandler

from src.seedwork.application.commands import exec_command as command
from src.transactions.domain.entities import Transaction
from src.seedwork.infraestructure.uow import UnitOfWorkPort
from src.transactions.application.mappers import MapperTransaction
from src.transactions.infrastructure.repositories import TransactionRepository

@dataclass
class SaveTransaction(Command):
    dni_landlord: str
    dni_tenant: str
    monetary_value: float
    type_lease: str
    contract_initial_date: date
    contract_final_date: date    
    
class SaveTransactionHandler(SaveTransactionBaseHandler):
    def handle(self, command: SaveTransaction):
        transaction_dto = TransactionAppDTO(
            dni_landlord=command.dni_landlord,
            dni_tenant=command.dni_tenant,
            monetary_value=command.monetary_value,
            type_lease=command.type_lease,
            contract_initial_date=command.contract_initial_date,
            contract_final_date=command.contract_final_date           
        )
        
        # evaluate
        transaction: Transaction = self.transaction_factory.create_object(
            transaction_dto, MapperTransaction())
        
        transaction.create_transaction(transaction)
        
        repository = self.repo_factory.create_object(
            TransactionRepository.__class__
        )
        
        UnitOfWorkPort.register_batch(repository.add, transaction)
        
        UnitOfWorkPort.commit()
        
        
@command.register(SaveTransaction)
def exec_command_save_transaction(command: SaveTransaction):
    handler = SaveTransactionHandler()
    handler.handle(command)

## agregando asincronismo
@dataclass
class SaveTransactionAsincronic(Command):    
    dni_landlord: str
    dni_tenant: str
    monetary_value: float
    type_lease: str
    contract_initial_date: date
    contract_final_date: date    
    
class SaveTransactionAsincronicHandler(SaveTransactionBaseHandler):
    def handle(self, command: SaveTransaction):
        print("creamos el transaction_dto en el handler de saveTransactionAsincronoHandler")
        transaction_dto = TransactionAppDTO(
            dni_landlord=command.dni_landlord,
            dni_tenant=command.dni_tenant,
            monetary_value=command.monetary_value,
            type_lease=command.type_lease,
            contract_initial_date=command.contract_initial_date,
            contract_final_date=command.contract_final_date           
        )
        
        # evaluate
        transaction: Transaction = self.transaction_factory.create_object(
            transaction_dto, MapperTransaction())
        
        transaction.create_transaction(transaction)
        
        repository = self.repo_factory.create_object(
            TransactionRepository.__class__
        )
        
        UnitOfWorkPort.register_batch(repository.addAsincronic, transaction)
        
        UnitOfWorkPort.commit()
        
        
@command.register(SaveTransactionAsincronic)
def exec_command_save_transaction_asincronic(command: SaveTransactionAsincronic):
    print("registrado el comando SaveTransactionAsincronic")
    handler = SaveTransactionAsincronicHandler()
    handler.handle(command)
        