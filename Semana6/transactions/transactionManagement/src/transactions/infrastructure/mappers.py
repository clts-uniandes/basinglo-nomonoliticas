from src.seedwork.domain.repositories import Mapper
from src.transactions.domain.entities import Transaction
from .dto import Transaction as TransactionDTO

class TransactionMapper(Mapper):

    def find_type(self) -> type:
        return Transaction.__class__
    
    def entity_to_dto(self, entity: Transaction) -> TransactionDTO:
        transaction_dto = TransactionDTO()
        transaction_dto.id = str(entity.id)
        transaction_dto.dni_landlord = entity.dni_landlord
        transaction_dto.dni_tenant = entity.dni_tenant
        transaction_dto.id_property = entity.id_property
        transaction_dto.monetary_value = entity.monetary_value
        transaction_dto.type_lease = entity.type_lease
        transaction_dto.contract_initial_date = entity.contract_initial_date
        transaction_dto.contract_final_date = entity.contract_final_date        
        transaction_dto.createdAt = entity.created_at
        return transaction_dto
    
    def dto_to_entity(self, dto: TransactionDTO) -> TransactionDTO:
        transaction = Transaction(id=dto.id, dni_landlord=dto.dni_landlord, dni_tenant=dto.dni_tenant, id_property=dto.id_property, monetary_value=dto.monetary_value, type_lease=dto.type_lease,
                             contract_initial_date=dto.contract_initial_date, contract_final_date=dto.contract_final_date, created_at=dto.createdAt)
        return transaction

