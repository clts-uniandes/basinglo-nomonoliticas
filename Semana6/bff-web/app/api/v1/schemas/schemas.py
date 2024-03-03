from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

# examples

class Transaction(BaseModel):
    buyer_id: str
    seller_id: str
    amount: int
    realization_date: datetime
    notes: Optional[str]

class Login(BaseModel):
    username: str
    password: str

class GenericResponse(BaseModel):
    msg: str

class TransactionDetailResponse(Transaction):
    id: int

class TransactionsResponse(BaseModel):
    data: List[TransactionDetailResponse]
    #total_pages: int

class LoginResponse(BaseModel):
    token: str
    