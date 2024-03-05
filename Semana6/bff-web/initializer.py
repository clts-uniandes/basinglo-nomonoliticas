from fastapi import FastAPI

from app.api.v1 import auth as auth_api
from app.api.v1 import transactions as transactions_api
from app.api import health as health_api

from app.modules.auth.application.queries.get_access import GetAccess
from app.modules.auth.infrastructure.rest_repository import AuthenticationRepository
from app.modules.transaction.application.queries.get_transaction import GetTransactions
from app.modules.transaction.application.commands.create_transaction import (
    CreateTransaction,
)
from app.modules.transaction.infrastructure.repositories import TransactionRepository
from app.modules.health.application.get_health import GetHealth


class Initializer:
    def __init__(self, app: FastAPI):
        self.app = app

    def setup(self):
        self.init_health_module()
        self.init_auth_module()
        self.init_transaction_module()

    def init_health_module(self):
        get_health = GetHealth()
        health_api.initialize(get_health)
        self.app.include_router(health_api.router)

    def init_auth_module(self):
        rest_repository = AuthenticationRepository()
        get_access = GetAccess(rest_repository)
        auth_api.initialize(get_access)
        self.app.include_router(auth_api.router)

    def init_transaction_module(self):
        rest_repository = TransactionRepository()
        get_transactions = GetTransactions(rest_repository)
        create_transaction = CreateTransaction(rest_repository)
        transactions_api.initialize(get_transactions, create_transaction)
        self.app.include_router(transactions_api.router)
