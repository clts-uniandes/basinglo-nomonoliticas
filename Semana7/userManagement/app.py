from flask import Flask
from os import environ as env
from datetime import timedelta

def import_alchemy_models():
    import src.modules.auth.infrastructure.dto
    import src.modules.users.infrastructure.dto

def register_handlers():
    import src.modules.auth.application
    import src.modules.users.application

def config_app():
    # init flask app
    flask_app = Flask(__name__)
    flask_app.secret_key = '61e7b756-8b90-482c-826c-64dae8d4ca2c'
    #app.register_blueprint(users_bp)

    user = env.get("DB_USER", "postgres")
    password = env.get("DB_PASSWORD", "postgres")
    host = env.get("DB_HOST", "users")
    port = env.get("DB_PORT", "5432")
    db_name = env.get("DB_NAME", "users")
    db_driver = env.get("DB_DRIVER", "postgresql")
    flask_app.config["DEBUG"] = True
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = f"{db_driver}://{user}:{password}@{host}:{port}/{db_name}"
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    flask_app.permanent_session_lifetime = timedelta(minutes=0)
    #flask_app.config['SESSION_TYPE'] = 'filesystem'

    from src.config.db import init_db
    init_db(flask_app)

    from src.config.db import db
    import_alchemy_models()
    register_handlers()

    with flask_app.app_context():
        db.create_all()

    from src.api.auth import auth_bp
    #from src.api.users import users_bp
    flask_app.register_blueprint(auth_bp)
    #flask_app.register_blueprint(users_bp)

    return flask_app

app = config_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
