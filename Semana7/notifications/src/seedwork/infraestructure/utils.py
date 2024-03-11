import time
import os

def time_millis():
    return int(time.time() * 1000)

def broker_host():
    return os.getenv('BROKER_PATH', default="localhost")

def broker_token():
    return os.getenv('BROKER_TOKEN', default="")

def broker_tenant():
    return os.getenv('BROKER_TENANT', default="")

def broker_namespace():
    return os.getenv('BROKER_NAMESPACE', default="")
