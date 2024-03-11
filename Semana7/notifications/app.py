import threading
import src.modules.auth.infrastructure.consumers as auth
import src.modules.notifications.infrastructure.consumers as notification

import src.modules.sagas.infrastructure.consumers as sagas

from flask import Flask
from os import environ as env

def config_app():
    # init flask app
    flask_app = Flask(__name__)
    flask_app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    flask_app.config["DEBUG"] = True
    from src.api.notifications import notification_bp
    flask_app.register_blueprint(notification_bp)

    # auth.subscribe_to_events()

    notification.subscribe_to_create_notification_command()
    notification.subscribe_to_reverse_notification_command()

    # PASO 0
    sagas.subscribe_to_start_saga_transaction_command()

    # PASO 1
    sagas.subscribe_to_created_notification_event()
    sagas.subscribe_to_failed_notification_event()

    # PASO 2
    sagas.subscribe_to_created_transaction_event()
    sagas.subscribe_to_failed_transaction_event()

    # PASO 3
    sagas.subscribe_to_failed_updated_property_event()
    sagas.subscribe_to_failed_updated_property_event()

    return flask_app

app = config_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)






