class InvalidParameterException(Exception):
    def __init__(self, message):
        super(InvalidParameterException, self).__init__(message)


class ResourceExistsException(Exception):
    def __init__(self, message):
        super(ResourceExistsException, self).__init__(message)


class ResourceNotFoundException(Exception):
    def __init__(self, message):
        super(ResourceNotFoundException, self).__init__(message)


class UserNotAuthorizedException(Exception):
    def __init__(self, message="User not authorized"):
        super(UserNotAuthorizedException, self).__init__(message)


class TokenNotFoundException(Exception):
    def __init__(self, message="Token not found"):
        super(TokenNotFoundException, self).__init__(message)


class PreconditionFailedException(Exception):
    def __init__(self, message):
        super(PreconditionFailedException, self).__init__(message)


class CustomException(Exception):
    def __init__(self, message="Error", status_code=500):
        super(CustomException, self).__init__(message)
        self.status_code = status_code
