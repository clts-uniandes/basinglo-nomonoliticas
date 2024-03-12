import uuid
 
from pulsar.schema import Long, String, Record
from src.seedwork.infraestructure.utils import time_millis
 
class Message(Record):
    # These values are useless due to Python Pulsar ignoring inherited values, consider deleting them
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()

    # def __init__(self, *args, id=None, **kwargs):
    #    super().__init__(*args, id=id, **kwargs)