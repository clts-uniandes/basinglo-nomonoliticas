from http import HTTPStatus
from flask import request

from src.seedwork.presentation.api import crear_blueprint
from src.modules.users.application.commands.save_personal_information import SavePersonalInfo
from src.modules.users.application.mappers import MapperUsersDTOJson
from src.seedwork.application.commands import exec_command
from src.seedwork.domain.exceptions import DomainException

users_bp = crear_blueprint('users', '/users')

@users_bp.route("register", methods=["POST"])
def register_credential():
    try:
        pi_dict = request.json
        pi_map = MapperUsersDTOJson()
        pi_dto = pi_map.external_to_dto(pi_dict)
        command = SavePersonalInfo(id_credential=pi_dto.id_credential,
            email=pi_dto.email,
            dni=pi_dto.dni,
            fullName=pi_dto.fullName,
            phoneNumber=pi_dto.phoneNumber,)
        exec_command(command)
        return { 'msg': 'Data saved'}, HTTPStatus.ACCEPTED
    except DomainException as e:
        return { 'msg': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR
    except Exception as e:
        return { 'msg': str(e)}, HTTPStatus.BAD_REQUEST
   

# @users_bp.route("/<string:user_id>", methods=["GET"])
# @handle_exceptions
# @is_authenticated
# def get_user(token, user_id):
#    pass
