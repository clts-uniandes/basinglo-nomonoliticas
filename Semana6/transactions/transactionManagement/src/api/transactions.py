from http import HTTPStatus
from flask import request
import pulsar
from src.seedwork.infraestructure import utils

from src.seedwork.presentation.api import crear_blueprint
from src.transactions.application.commands.save_transaction import SaveTransaction, SaveTransactionAsincronic
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
                               id_property=py_dto.id_property,
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
    

@transactions_bp.route("addCommand", methods=["POST"])
def add_transaction_asincronic():
    try:
        transaction_dict = request.json
        transaction_map = MapperTransactionDTOJson()
        py_dto = transaction_map.external_to_dto(transaction_dict)
        command = SaveTransactionAsincronic(dni_landlord=py_dto.dni_landlord,
                               dni_tenant=py_dto.dni_tenant,
                               id_property=py_dto.id_property,
                               monetary_value=py_dto.monetary_value,
                               type_lease=py_dto.type_lease,
                               contract_initial_date=py_dto.contract_initial_date,
                               contract_final_date=py_dto.contract_final_date)
        print("Vamos a llamar al comando ", command)
        exec_command(command)
        return { 'msg': 'Transaction saved'}, HTTPStatus.ACCEPTED
    except DomainException as e:
        return { 'msg': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR
    except Exception as e:
        return { 'msg': str(e)}, HTTPStatus.BAD_REQUEST
    

@transactions_bp.route("testPulsar", methods=["GET"])
def check_pulsar():
    print("Probando la conexion a Pulsar ", {utils.broker_host()})
    client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')    
    producer = client.create_producer('topico_prueba_andes')
    for i in range(5):
        producer.send(('Hola pulsar ddd -%d' % i).encode('utf-8'))
    client.close()
    print("Conexion exitosa")
    return { 'msg': 'Pulsar OK'}, HTTPStatus.ACCEPTED