from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, UUID4

# testing only

class GenericResponse(BaseModel):
    msg: str

# Transactions, unused

class Transaction(BaseModel):
    buyer_id: str
    seller_id: str
    property_id: UUID4
    amount: int
    realization_date: datetime
    notes: Optional[str]

class TransactionDetailResponse(Transaction):
    id: int

class TransactionsResponse(BaseModel):
    data: List[TransactionDetailResponse]

# Users, active

class Login(BaseModel):
    username: str
    password: str

class NewUser(BaseModel):
    username: str
    password: str
    email: str
    dni: str
    fullName: str
    phoneNumber: str

class LoginResponse(BaseModel):
    msg: str

# Record saga, active

class NewSellTransaction(BaseModel):
    dni_landlord : str
    dni_tenant : str
    id_property : str
    monetary_value : str
    contract_initial_date : str
    contract_final_date : str

class RecordResponse(BaseModel):
    msg: str 