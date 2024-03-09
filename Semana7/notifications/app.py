import threading
import src.modules.auth.infrastructure.consumers as auth

from flask import Flask
from os import environ as env

def config_app():
    # init flask app
    flask_app = Flask(__name__)
    flask_app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    flask_app.config["DEBUG"] = True

    from src.api.notifications import notification_bp
    flask_app.register_blueprint(notification_bp)

    #auth.subscribe_to_events()

    return flask_app

app = config_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
