from src.seedwork.domain.exceptions import FactoryException

class NoImplementationForFactoryTypeException(FactoryException):
    def __init__(self, message='No implementation for factory type'):
        self.__message = message
    def __str__(self):
        return str(self.__message)