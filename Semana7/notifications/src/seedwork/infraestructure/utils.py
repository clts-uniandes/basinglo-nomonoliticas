import os

def broker_host():
    return os.getenv('BROKER_PATH', default="localhost")

def broker_token():
    return os.getenv('BROKER_TOKEN', default="")

def broker_tenant():
    return os.getenv('BROKER_TENANT', default="")

def broker_namespace():
    return os.getenv('BROKER_NAMESPACE', default="")

def send_email(email):
    print('======== Sent email to user =========')
    print(email)
    print('=========================================')
