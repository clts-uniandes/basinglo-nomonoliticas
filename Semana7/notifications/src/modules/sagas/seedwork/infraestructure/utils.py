import os
import datetime
import time

def broker_host():
    return os.getenv('BROKER_PATH', default="localhost")

def send_email(email):
    print('======== Sent email to user =========')
    print(email)
    print('=========================================')

def time_millis():
    return int(time.time() * 1000)