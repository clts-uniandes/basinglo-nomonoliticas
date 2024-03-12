import time
import os
import datetime
import requests
import json
from fastavro.schema import parse_schema
from pulsar.schema import AvroSchema, Record, String, Integer

epoch = datetime.datetime.utcfromtimestamp(0)
BROKER_URL = "BROKER_URL"
API_URL = "API_URL"
PULSAR_TOKEN = "PULSAR_TOKEN"


class Transaction(Record):
    buyer_id = String()
    seller_id = String()
    amount = Integer()
    realization_date = String()
    notes = String()


def time_millis():
    return int(time.time() * 1000)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


def millis_to_datetime(millis):
    return datetime.datetime.fromtimestamp(millis / 1000.0)


def broker_url():
    return os.getenv(BROKER_URL, default="pulsar://localhost:6650")


def broker_api_url():
    return os.getenv(API_URL, default="http://localhost:8080")


def broker_token():
    return os.getenv(PULSAR_TOKEN, default="none")


def check_schema_registry(full_topic: str) -> dict:
    print("using token: " + broker_token())
    json_registry = requests.get(
        f"{broker_api_url()}/admin/v2/schemas/{full_topic}/schema",
        headers={"Authorization": f"Bearer {broker_token()}"},
    )
    print("pulsar schema received:" + json_registry.text)
    return json.loads(json_registry.json().get("data", {}))


def get_avro_schema_from_dict(json_schema: dict) -> AvroSchema:
    schema_definition = parse_schema(json_schema)
    return AvroSchema(None, schema_definition=schema_definition)
    # return AvroSchema(Transaction())


# others
def build_request_uri(url: str, endpoint: str) -> str:
    return f"{url}/{endpoint}"
