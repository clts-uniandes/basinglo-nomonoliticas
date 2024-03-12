from dataclasses import dataclass, field
from .events import DomainEvent
from .mixins import ValidateRulesMixin
from .rules import ImmutableId
from .exceptions import ImmutableIdException
from datetime import datetime
import uuid

@dataclass
class Entity:
    id: uuid.UUID = field(hash=True)
    _id: uuid.UUID = field(init=False, repr=False, hash=True)
    created_at: datetime =  field(default=datetime.now())

    @classmethod
    def next_id(self) -> uuid.UUID:
        return uuid.uuid4()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: uuid.UUID) -> None:
        if not ImmutableId(self).is_valid():
            raise ImmutableIdException()
        self._id = self.next_id()
        

@dataclass
class AgregationRoot(Entity, ValidateRulesMixin):
    events: list[DomainEvent] = field(default_factory=list)

    def add_event(self, event: DomainEvent):
        self.events.append(event)
        print(f'{type(event).__name__}Domain was published')
    
    def clear_events(self):
        self.events = list()


@dataclass
class Location(Entity):
    def __str__(self) -> str:
        ...
