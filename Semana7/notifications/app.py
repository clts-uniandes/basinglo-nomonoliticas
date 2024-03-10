import threading
import src.modules.auth.infrastructure.consumers as auth
import src.modules.notifications.infrastructure.consumers as notifications
import src.modules.transactions.infrastructure.consumers as transactions
import src.modules.properties.infrastructure.consumers as properties

from flask import Flask
from os import environ as env

def config_app():
    # init flask app
    flask_app = Flask(__name__)
    flask_app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    flask_app.config["DEBUG"] = True
    from src.api.notifications import notification_bp
    flask_app.register_blueprint(notification_bp)

    auth.subscribe_to_events()
    notifications.subscribe_to_commands()
    transactions.subscribe_to_events()
    transactions.subscribe_to_commands()
    properties.subscribe_to_events()
    properties.subscribe_to_commands()
    
    return flask_app

app = config_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)






