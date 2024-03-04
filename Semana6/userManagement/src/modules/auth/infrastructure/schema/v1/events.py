from pulsar.schema import *

class UserCreatedEvent(Record):
    email = String()
