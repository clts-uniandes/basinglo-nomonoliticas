from functools import singledispatch
from abc import ABC, abstractmethod
from dataclasses import dataclass


class Query(ABC):
    ...

@dataclass
class QueryResult:
    result: None

class QueryHandler(ABC):
    @abstractmethod
    def handle(self, query: Query) -> QueryResult:
        raise NotImplementedError()

@singledispatch
def exec_query(query):
    raise NotImplementedError(f'Query implementation type {type(query).__name__} not available')
