from http import HTTPStatus
from flask import request

from ..seedwork.presentation.api import crear_blueprint
from ..modules.auth.application.commands.register_credential import RegisterCredential
from ..modules.auth.application.queries.authenticate_user import AuthenticateUser
from ..modules.auth.application.mappers import MapperAuthDTOJson
from src.seedwork.application.commands import exec_command
from src.seedwork.application.queries import exec_query
from src.seedwork.domain.exceptions import DomainException

auth_bp = crear_blueprint("auth", "/auth")


@auth_bp.route("signup", methods=["POST"])
def register_credential():
    try:
        credential_dict = request.json
        credential_map = MapperAuthDTOJson()
        credential_dto = credential_map.external_to_dto(credential_dict)
        command = RegisterCredential(
            username=credential_dto.username,
            password=credential_dto.password,
            email=credential_dto.email,
            dni=credential_dto.dni,
            fullName=credential_dto.fullName,
            phoneNumber=credential_dto.phoneNumber,
        )
        exec_command(command)
        return {"msg": "Credential created"}, HTTPStatus.ACCEPTED
    except DomainException as e:
        return {"msg": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR
    except Exception as e:
        return {"msg": str(e)}, HTTPStatus.BAD_REQUEST


@auth_bp.route("signin", methods=["POST"])
def authenticate_user():
    try:
        data = request.get_json()
        exec_query(AuthenticateUser(data["username"], data["password"]))
        return {"msg": "Valid credentials"}, HTTPStatus.OK
    except Exception as e:
        return {"msg": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR
