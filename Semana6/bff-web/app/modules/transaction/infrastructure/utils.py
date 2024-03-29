import time
import os
import datetime
import requests
import json
from fastavro.schema import parse_schema
from pulsar.schema import AvroSchema, Record, String, Integer

epoch = datetime.datetime.utcfromtimestamp(0)
PULSAR_HOST = 'PULSAR_HOST'

class Transaction(Record):
    buyer_id =  String()
    seller_id = String()
    amount = Integer()
    realization_date = String()
    notes = String()

def time_millis():
    return int(time.time() * 1000)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

def millis_to_datetime(millis):
    return datetime.datetime.fromtimestamp(millis/1000.0)

def broker_host():
    return os.getenv(PULSAR_HOST, default="localhost")

def check_schema_registry(full_topic: str) -> dict:
    json_registry = requests.get(f'http://{broker_host()}:8080/admin/v2/schemas/{full_topic}/schema')
    print("pulsar schema received:"+json_registry.text)
    return json.loads(json_registry.json().get('data',{}))

def get_avro_schema_from_dict(json_schema: dict) -> AvroSchema:
    schema_definition = parse_schema(json_schema)
    return AvroSchema(None, schema_definition=schema_definition)
    #return AvroSchema(Transaction())

# others
def build_request_uri(host: str, endpoint: str) -> str:
    return f"https://{host}/{endpoint}"
