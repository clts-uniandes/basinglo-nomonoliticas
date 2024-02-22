from ....users.domain.entities import User
from ....users.domain.schemas import UserSchema
from src.api.utils.decorators import db_session
from src.api.utils.exceptions import ResourceNotFoundException, UserNotAuthorizedException

@db_session
def _get_user(session, token, user_id):
    user = session.query(User).filter(User.id == user_id).first()
    if user is None:
        raise ResourceNotFoundException("User not found.")
    else:
        if(user.token != token):
            raise UserNotAuthorizedException("Token not valid.")
        return UserSchema().dump(user)
    