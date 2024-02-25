from http import HTTPStatus
from flask import request

from ..seedwork.presentation.api import crear_blueprint
from ..api.utils.decorators import handle_exceptions
from ..modules.auth.application.commands.register_credential import RegisterCredential
from ..modules.auth.application.queries.authenticate_user import _authenticate_user
from ..modules.auth.application.mappers import MapperAuthDTOJson
from src.seedwork.application.commands import exec_command

auth_bp = crear_blueprint('auth', '/auth')

@auth_bp.route("signup", methods=["POST"])
def register_credential():
    credential_dict = request.json
    credential_map = MapperAuthDTOJson()
    credential_dto = credential_map.externo_a_dto(credential_dict)
    command = RegisterCredential(username=credential_dto.username, password=credential_dto.password)
    exec_command(command)
    return { 'msg': 'Credential created'}, HTTPStatus.CREATED


@auth_bp.route("signin", methods=["POST"])
@handle_exceptions
def authenticate_user():
    return _authenticate_user(request), HTTPStatus.OK
