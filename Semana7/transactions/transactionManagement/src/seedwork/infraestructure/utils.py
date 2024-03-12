import time
import os
import datetime

BROKER_URL = "BROKER_URL"
PULSAR_TOKEN = "PULSAR_TOKEN"

def time_millis():
    return int(time.time() * 1000)

def broker_host():
    return os.getenv('BROKER_HOST', default="localhost")

def topic_trans_saved():
    return os.getenv('TOPIC_TRANS_SAVED', default="topic_transaction_saved")

def topic_consumer():
    return os.getenv('TOPIC_CONSUMER', default="topic_transaction_consumer")

def millis_a_datetime(millis):
    return datetime.datetime.fromtimestamp(millis/1000.0)

def enable_transaction():
    return os.getenv('ENABLE', default= True)

def topic_saga():
    return os.getenv('TOPIC_SAGA', default="topic_transaction_saga")

def topic_saga_response():
    return os.getenv('TOPIC_SAGA_RESPONSE', default="topic_transaction_saga_response")

def broker_url():
    return os.getenv(BROKER_URL, default="pulsar://broker_pulsar:6650")


def broker_token():
    return os.getenv(PULSAR_TOKEN, default="")



