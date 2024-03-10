from flask import Flask
from os import environ as env
from datetime import timedelta

def import_alchemy_models():
    import src.modules.auth.infrastructure.dto
    import src.modules.users.infrastructure.dto

def register_handlers():
    import src.modules.auth.application
    import src.modules.users.application

def start_message_consumers(app):
    
    import threading
    import src.modules.auth.infrastructure.consumers as authentication
    import src.modules.users.infrastructure.consumers as users

    # Events listener (optional); disable to reduce mem comsumption
    #threading.Thread(target=authentication.event_topic_subscribe).start()
    #threading.Thread(target=users.event_topic_subscribe).start()
    #tutorial 8 args with start?

    # Commands listener
    threading.Thread(target=authentication.command_event_subscribe).start()
    #threading.Thread(target=users.command_event_subscribe).start()
    

def config_app():
    
    flask_app = Flask(__name__)
    flask_app.secret_key = '61e7b756-8b90-482c-826c-64dae8d4ca2c'
    # flask_app.config['SESSION_TYPE'] = 'filesystem' # optional?
    # flask_app.config['TESTING'] = configuracion.get('TESTING') # might be required
    flask_app.permanent_session_lifetime = timedelta(minutes=0) # make cookie sessions useless

    user = env.get("DB_USER", "postgres")
    password = env.get("DB_PASSWORD", "postgres")
    host = env.get("DB_HOST", "users")
    port = env.get("DB_PORT", "5432")
    db_name = env.get("DB_NAME", "users")
    db_driver = env.get("DB_DRIVER", "postgresql")
    flask_app.config["DEBUG"] = True
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = f"{db_driver}://{user}:{password}@{host}:{port}/{db_name}"
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    from src.config.db import init_db
    init_db(flask_app)

    from src.config.db import db
    import_alchemy_models()
    register_handlers()

    with flask_app.app_context():
        db.create_all()
        if not flask_app.config.get('TESTING'):
            start_message_consumers(flask_app)

    from src.api.auth import auth_bp
    #from src.api.users import users_bp
    flask_app.register_blueprint(auth_bp)
    #flask_app.register_blueprint(users_bp)

    @flask_app.route("/health")
    def health():
        return {"status": "ok"}

    return flask_app

app = config_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
