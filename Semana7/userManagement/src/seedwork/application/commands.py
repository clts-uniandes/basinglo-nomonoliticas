from functools import singledispatch
from abc import ABC, abstractmethod

class Command:
    ...

class CommandHandler(ABC):
    @abstractmethod
    def handle(self, command: Command):
        raise NotImplementedError()

@singledispatch
def exec_command(command):
    raise NotImplementedError(f'Command implementation type {type(command).__name__} not available')
