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

    threading.Thread(target=notification.subscribe_to_create_notification_command).start()
    threading.Thread(target=notification.subscribe_to_reverse_notification_command).start()

    # PASO 0
    threading.Thread(target=sagas.subscribe_to_start_saga_transaction_command).start()

    # PASO 1
    threading.Thread(target=sagas.subscribe_to_created_notification_event).start()
    threading.Thread(target=sagas.subscribe_to_failed_notification_event).start()

    # PASO 2
    threading.Thread(target=sagas.subscribe_to_created_transaction_event).start()
    threading.Thread(target=sagas.subscribe_to_failed_transaction_event).start()

    # PASO 3
    threading.Thread(target=sagas.subscribe_to_updated_property_event).start()
    threading.Thread(target=sagas.subscribe_to_failed_updated_property_event).start()

    return flask_app

app = config_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)






