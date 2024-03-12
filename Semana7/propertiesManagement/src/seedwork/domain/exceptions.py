from .rules import BusinessRule

class DomainException(Exception):
    ...

class ImmutableIdException(DomainException):
    def __init__(self, message='Id immutable'):
        self.__message = message
    def __str__(self):
        return str(self.__message)

class BusinessRuleExcepcion(DomainException):
    def __init__(self, regla: BusinessRule):
        self.regla = regla

    def __str__(self):
        return str(self.regla)

class FactoryException(DomainException):
    def __init__(self, message):
        self.__message = message
    def __str__(self):
        return str(self.__message)