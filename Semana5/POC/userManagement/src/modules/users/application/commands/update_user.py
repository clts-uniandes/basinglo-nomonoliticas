from ....users.domain.entities import User
from ....users.domain.schemas import UserSchema
from src.api.utils.decorators import db_session
from src.api.utils.exceptions import InvalidParameterException, ResourceNotFoundException, UserNotAuthorizedException

@db_session
def _update_user(session, token, user_id, request):
    data = request.get_json()
    
    if data is None:
        raise InvalidParameterException("Request body is empty.")

    user = session.query(User).filter(User.id == user_id).first()
    if user is None:
        raise ResourceNotFoundException("User not found.")
    else:
        if(user.token != token):
            raise UserNotAuthorizedException("Token not valid.")
        
        if 'status' in data:
            user.status = data['status']
        if 'dni' in data:
            user.dni = data['dni']
        if 'fullName' in data:
            user.fullName = data['fullName']
        if 'phoneNumber' in data:
            user.phoneNumber = data['phoneNumber']
        session.commit()

    return UserSchema().dump(user)

@db_session
def _save_personal_info(session, token, user_dto, request):
    data = request.get_json()
    
    if data is None:
        raise InvalidParameterException("Request body is empty.")
    
    user = session.query(User).filter(User.id == user_id).first()
    if user is None:
        raise ResourceNotFoundException("User not found.")



@dataclass
class RegisterPersonalInformation(Command):
    email = str
    dni = int
    fullName = str
    phoneNumber = str
    
class RegisterPersonalInformationHandler()