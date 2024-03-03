from dataclasses import dataclass, field
from datetime import date
from src.seedwork.application.dto import DTO

@dataclass(frozen=True)
class TransactionAppDTO(DTO):
    dni_landlord: str
    dni_tenant: str
    monetary_value: float
    type_lease: str
    contract_initial_date: date
    contract_final_date: date
    