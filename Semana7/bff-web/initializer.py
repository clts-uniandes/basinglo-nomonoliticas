from fastapi import FastAPI

from app.api.v1 import user as user_api
from app.api.v1 import records as records_api
from app.api import health as health_api
from app.api import main_page as main_page_api

from app.modules.user.application.queries.get_access import GetAccess
from app.modules.user.application.commands.register_user import RegisterUser
from app.modules.user.infrastructure.repositories import UsersRepository
from app.modules.record.application.commands.record_sell_transaction import RecordSellTransaction
from app.modules.record.infrastructure.repositories import RecordRepository
from app.modules.health.application.get_health import GetHealth


class Initializer:
    def __init__(self, app: FastAPI):
        self.app = app

    def setup(self):
        self.init_health_module()
        self.init_main_page_module()
        self.init_user_module()
        #self.init_transaction_module()
        self.init_notification_saga_module()
        
    def init_health_module(self):
        get_health = GetHealth()
        health_api.initialize(get_health)
        self.app.include_router(health_api.router)
    
    def init_main_page_module(self):
        #rest_repository = AuthenticationRepository()
        #get_access = GetAccess(rest_repository)
        main_page_api.initialize()
        self.app.include_router(main_page_api.router)

    def init_user_module(self):
        repository = UsersRepository()
        get_access = GetAccess(repository)
        register_user = RegisterUser(repository)
        user_api.initialize(get_access, register_user)
        self.app.include_router(user_api.router)

    def init_notification_saga_module(self):
        repository = RecordRepository()
        record_sell_transaction = RecordSellTransaction(repository)
        records_api.initialize(record_sell_transaction)
        self.app.include_router(records_api.router)
