from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from src.transactions.domain.events import TransactionCreated
from src.seedwork.domain.entities import AgregationRoot

@dataclass
class Transaction(AgregationRoot):
    dni_landlord: str = field(default=None)
    dni_tenant: str = field(default=None)
    monetary_value: float = field(default=None)
    type_lease: str = field(default=None)
    contract_initial_date: date = field(default=None)
    contract_final_date: date = field(default=None)


    def create_property(self, transaction: Transaction):
        self.dni_landlord = transaction.dni_landlord
        self.dni_tenant = transaction.dni_tenant
        self.monetary_value = transaction.monetary_value
        self.type_lease = transaction.type_lease
        self.contract_initial_date = transaction.contract_initial_date
        self.contract_final_date = transaction.contract_final_date        

        self.add_event(TransactionCreated(id_transactionCreated=self.id, created_at=self.created_at))