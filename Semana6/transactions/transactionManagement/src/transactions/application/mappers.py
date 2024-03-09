from src.seedwork.application.dto import Mapper as AppMap
from src.seedwork.domain.repositories import Mapper as RepoMap
from src.transactions.domain.entities import Transaction
from .dto import TransactionAppDTO

class MapperTransactionDTOJson(AppMap):
    def external_to_dto(self, external: dict) -> TransactionAppDTO:
        transaction_dto = TransactionAppDTO(
            dni_landlord= external['dni_landlord'],
            dni_tenant= external['dni_tenant'],
            id_property = external['id_property'],
            monetary_value= external['monetary_value'],            
            contract_initial_date= external['contract_initial_date'],
            contract_final_date= external['contract_final_date'],            
        )
        return transaction_dto
    
    def dto_to_external(self, dto:TransactionAppDTO) -> dict:
        return dto.__dict__
    


class MapperTransaction(RepoMap):
    
    def find_type(self) -> type:
        return Transaction.__class__
    
    def entity_to_dto(self, entity: Transaction) -> TransactionAppDTO:
        return TransactionAppDTO(entity.dni_landlord,entity.dni_tenant,entity.id_property,entity.monetary_value,entity.contract_initial_date,entity.contract_final_date)
    
    def dto_to_entity(self, dto: TransactionAppDTO) -> Transaction:
        transaction = Transaction()
        transaction.dni_landlord = dto.dni_landlord
        transaction.dni_tenant = dto.dni_tenant
        transaction.id_property = dto.id_property
        transaction.monetary_value = dto.monetary_value        
        transaction.contract_initial_date = dto.contract_initial_date
        transaction.contract_final_date = dto.contract_final_date
                
        return transaction