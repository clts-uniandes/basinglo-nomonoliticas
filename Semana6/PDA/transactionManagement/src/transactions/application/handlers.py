from src.seedwork.application.handlers import Handler
from src.seedwork.application.commands import exec_command
from src.seedwork.application.handlers import Handler
from .commands.save_transaction import SaveTransaction

class DomainTransactionHandler(Handler):
    
    @staticmethod
    def handle_transaction_created(event):
        print(event)
        command = SaveTransaction(
            dni_landlord=event.dni_landlord,
            dni_tenant=event.dni_tenant,
            monetary_value=event.monetary_value,
            type_lease=event.type_lease,
            contract_initial_date=event.contract_initial_date,
            contract_final_date=event.contract_final_date,            
        )
        exec_command(command)