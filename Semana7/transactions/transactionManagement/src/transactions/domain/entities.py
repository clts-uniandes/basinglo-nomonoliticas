from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from src.transactions.domain.events import TransactionCreated
from src.seedwork.domain.entities import AgregationRoot

@dataclass
class Transaction(AgregationRoot):
    dni_landlord: str = field(default=None)
    dni_tenant: str = field(default=None)
    id_property: str = field(default=None)
    monetary_value: float = field(default=None)    
    contract_initial_date: date = field(default=None)
    contract_final_date: date = field(default=None)


    def create_transaction(self, transaction: Transaction):
        self.dni_landlord = transaction.dni_landlord
        self.dni_tenant = transaction.dni_tenant
        self.id_property = transaction.id_property
        self.monetary_value = transaction.monetary_value        
        self.contract_initial_date = transaction.contract_initial_date
        self.contract_final_date = transaction.contract_final_date        

        self.add_event(TransactionCreated(id_transactionCreated=self.id, created_at=self.created_at))

@dataclass
class ResponseTransaction(AgregationRoot):
    id_transaction: str = field(default=None)
    status: str = field(default=None)
    created_at: str = field(default=None)


    def create_response(self, response: ResponseTransaction):
        self.id_transaction = response.id_transaction
        self.status = response.status
        self.created_at = response.created_at

@dataclass
class ResponseSaga(AgregationRoot):
    status: str = field(default=None)

    def create_response_saga(self, response:ResponseSaga):
        self.status = response.status