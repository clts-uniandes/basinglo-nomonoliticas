from functools import singledispatch
from abc import ABC, abstractmethod

class Projection(ABC):
    @abstractmethod
    def execute(self):
        ...

class ProjectionHandler(ABC):
    @abstractmethod
    def handle(self, projection: Projection):
        ...

@singledispatch
def execute_projection(projection):
    raise NotImplementedError(f'No existe implementación para la proyección de tipo {type(projection).__name__}')