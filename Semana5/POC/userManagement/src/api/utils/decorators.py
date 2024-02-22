from functools import wraps
from http import HTTPStatus

from ...config.db import SessionLocal
from .exceptions import CustomException
from .exceptions import InvalidParameterException
from .exceptions import PreconditionFailedException
from .exceptions import ResourceExistsException
from .exceptions import ResourceNotFoundException
from .exceptions import TokenNotFoundException
from .exceptions import UserNotAuthorizedException

from flask import request

def handle_exceptions(func):
    """
    Decorator to handle exceptions
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        status_code = HTTPStatus.OK
        error = ""
        try:
            return func(*args, **kwargs)
        except ResourceNotFoundException as e:
            status_code = HTTPStatus.NOT_FOUND
            error = str(e)
        except InvalidParameterException as e:
            status_code = HTTPStatus.BAD_REQUEST
            error = str(e)
        except UserNotAuthorizedException as e:
            status_code = HTTPStatus.UNAUTHORIZED
            error = str(e)
        except ResourceExistsException as e:
            status_code = HTTPStatus.CONFLICT
            error = str(e)
        except PreconditionFailedException as e:
            status_code = HTTPStatus.PRECONDITION_FAILED
            error = str(e)
        except TokenNotFoundException as e:
            status_code = HTTPStatus.FORBIDDEN
            error = str(e)
        except CustomException as e:
            status_code = e.status_code
            error = str(e)
        except Exception as e:
            status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            error = str(e)
        finally:
            if status_code >= HTTPStatus.BAD_REQUEST:
                response_object = {
                    'msg': error
                }
                return response_object, status_code

    return wrapper


def db_session(func):
    """
    Decorator to create a database session
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        session = SessionLocal()
        try:
            result = func(session, *args, **kwargs)
            return result
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    return wrapper

def is_authenticated(func):
    """
    Decorator to check if user is authenticated
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        bearer_token = request.headers.get("Authorization")
        if bearer_token is not None and bearer_token.startswith("Bearer "):
            token = bearer_token.split(" ")[1]
            return func(token, *args, **kwargs)
        else:
            raise TokenNotFoundException("Token not found.")

    return wrapper
