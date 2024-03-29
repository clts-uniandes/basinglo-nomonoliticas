import time
import os

def time_millis():
    return int(time.time() * 1000)

def broker_host():
    return os.getenv('BROKER_HOST', default="localhost")

def topic():
    return os.getenv('TOPIC', default="topic_transaction")

def topic_consumer():
    return os.getenv('TOPIC_CONSUMER', default="topic_consumer_transaction")

