from http import HTTPStatus
from flask import request

from ..seedwork.presentation.api import crear_blueprint
from ..api.utils.decorators import handle_exceptions, is_authenticated
from ..modules.users.application.queries.get_user import _get_user
from ..modules.users.application.commands.update_user import _update_user

users_bp = crear_blueprint('users', '/users')

@users_bp.route("/<string:user_id>", methods=["PATCH"])
@handle_exceptions
@is_authenticated
def update_user(token, user_id):
    return _update_user(token, user_id, request), HTTPStatus.OK


@users_bp.route("/<string:user_id>", methods=["GET"])
@handle_exceptions
@is_authenticated
def get_user(token, user_id):
    return _get_user(token, user_id), HTTPStatus.OK
