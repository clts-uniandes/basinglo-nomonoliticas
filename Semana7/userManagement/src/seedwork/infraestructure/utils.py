import datetime
import os
import time

BROKER_URL = "BROKER_URL"
PULSAR_TOKEN = "PULSAR_TOKEN"

epoch = datetime.datetime.utcfromtimestamp(0)

def time_millis():
    return int(time.time() * 1000)

# def millis_to_datetime(millis):
#     return datetime.datetime.fromtimestamp(millis/1000.0)

# def unix_time_millis(dt):
#    return (dt - epoch).total_seconds() * 1000.0

#delete
def broker_host():
    return os.getenv('BROKER_PATH', default="localhost")

def broker_url():
    return os.getenv(BROKER_URL, default="pulsar://localhost:6650")

def broker_token():
    return os.getenv(PULSAR_TOKEN, default="none")