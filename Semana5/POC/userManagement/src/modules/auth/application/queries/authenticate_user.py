import datetime

from ....users.domain.entities import User
from ....auth.domain.schemas import EntitySchema
from src.api.utils.decorators import db_session
from src.api.utils.exceptions import InvalidParameterException, ResourceNotFoundException
from ....auth.infrastructure.utils import get_token, verify_password

@db_session
def _authenticate_user(session, request):
    data = request.get_json()

    if data is None:
        raise InvalidParameterException("Request body is empty.")

    username_request = data.get("username", None)
    password_request = data.get("password", None)

    if username_request is None or password_request is None:
        raise InvalidParameterException("Request body is not complete.")

    user = session.query(User).filter(User.username == username_request).first()
    if user is None:
        raise ResourceNotFoundException("Username not exists.")
    else:
        salt_password = user.salt
        password_user_to_check = user.password
        verify = verify_password(password_user_to_check, salt_password, password_request)
        if not verify:
            raise ResourceNotFoundException("Password is not correct.")
        else:
            user.token = get_token()
            today = datetime.datetime.now()
            user.expireAt = today + datetime.timedelta(minutes=30)
            session.commit()
            return EntitySchema().dump(user)
