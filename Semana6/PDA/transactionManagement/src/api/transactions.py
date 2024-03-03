from http import HTTPStatus
from flask import request

from src.seedwork.presentation.api import crear_blueprint
from src.transactions.application.commands.save_transaction import SaveTransaction
from src.transactions.application.mappers import MapperTransactionDTOJson
from src.seedwork.application.commands import exec_command
from src.seedwork.domain.exceptions import DomainException

transactions_bp = crear_blueprint('transactions', '/transactions')

@transactions_bp.route("add", methods=["POST"])
def add_transaction():
    try:
        transaction_dict = request.json
        transaction_map = MapperTransactionDTOJson()
        py_dto = transaction_map.external_to_dto(transaction_dict)
        command = SaveTransaction(dni_landlord=py_dto.dni_landlord,
                               dni_tenant=py_dto.dni_tenant,
                               monetary_value=py_dto.monetary_value,
                               type_lease=py_dto.type_lease,
                               contract_initial_date=py_dto.contract_initial_date,
                               contract_final_date=py_dto.contract_final_date)
        exec_command(command)
        return { 'msg': 'Transaction saved'}, HTTPStatus.ACCEPTED
    except DomainException as e:
        return { 'msg': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR
    except Exception as e:
        return { 'msg': str(e)}, HTTPStatus.BAD_REQUEST