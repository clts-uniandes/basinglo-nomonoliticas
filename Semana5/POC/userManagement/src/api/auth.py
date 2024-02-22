from http import HTTPStatus
from flask import request

from ..seedwork.presentation.api import crear_blueprint
from ..api.utils.decorators import handle_exceptions
from ..modules.auth.application.commands.register_user import _register_user
from ..modules.auth.application.commands.authenticate_user import _authenticate_user

auth_bp = crear_blueprint('auth', '/auth')

@auth_bp.route("signup", methods=["POST"])
@handle_exceptions
def register_user():
    return _register_user(request), HTTPStatus.CREATED


@auth_bp.route("signin", methods=["POST"])
@handle_exceptions
def authenticate_user():
    return _authenticate_user(request), HTTPStatus.OK
