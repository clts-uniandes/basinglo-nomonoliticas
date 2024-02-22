from ....users.domain.entities import User
from ....users.domain.schemas import UserSchema
from src.api.utils.decorators import db_session
from src.api.utils.exceptions import InvalidParameterException, PreconditionFailedException
from ....auth.infrastructure.utils import encrypt_password

@db_session
def _register_user(session, request):
    data = request.get_json()

    if data is None:
        raise InvalidParameterException("Request body is empty.")

    email_request = data.get("email", None)
    username_request = data.get("username", None)
    password_request = data.get("password", None)
    dni_request = data.get("dni", None)
    fullName_request = data.get("fullName", None)
    phoneNumber_request = data.get("phoneNumber", None)

    if username_request is None or password_request is None or email_request is None:
        raise InvalidParameterException("Request body is empty.")

    user = session.query(User).filter(User.username == username_request).first()
    if not user is None:
        raise PreconditionFailedException("Username already exists.")

    user = session.query(User).filter(User.email == email_request).first()
    if not user is None:
        raise PreconditionFailedException("Email already exists.")

    hashed_password, salt = encrypt_password(password_request)

    user = User(
        username=username_request,
        password=hashed_password,
        salt=salt,
        status="CREATED",
        email=email_request,
        dni=dni_request,
        fullName=fullName_request,
        phoneNumber=phoneNumber_request,
    )

    session.add(user)
    session.commit()

    return UserSchema().dump(user)
