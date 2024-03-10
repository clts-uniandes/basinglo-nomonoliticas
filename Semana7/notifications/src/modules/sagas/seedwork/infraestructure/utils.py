import os

def broker_host():
    return os.getenv('BROKER_PATH', default="localhost")

def send_email(email):
    print('======== Sent email to user =========')
    print(email)
    print('=========================================')
