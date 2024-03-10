from flask import Flask
from os import environ as env

def import_alchemy_models():
    import src.transactions.infrastructure.dto

def register_handlers():
    import src.transactions.application

def start_consumer():
    import threading
    import src.transactions.infrastructure.consumer as consumer
    threading.Thread(target=consumer.suscribirse_a_comandos).start()
    
def config_app():
    # init flask app
    flask_app = Flask(__name__)
    flask_app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    #app.register_blueprint(users_bp)

    user = env.get("DB_USER", "postgres")
    password = env.get("DB_PASSWORD", "postgres")
    host = env.get("DB_HOST", "transactions")
    port = env.get("DB_PORT", "5432")
    db_name = env.get("DB_NAME", "transactions")
    db_driver = env.get("DB_DRIVER", "postgresql")
    flask_app.config["DEBUG"] = True
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = f"{db_driver}://{user}:{password}@{host}:{port}/{db_name}"
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    #flask_app.config['SESSION_TYPE'] = 'filesystem'

    from src.config.db import init_db
    init_db(flask_app)

    from src.config.db import db
    import_alchemy_models()
    register_handlers()
    

    with flask_app.app_context():
        db.create_all()
        if not flask_app.config.get('TESTING'):
            start_consumer()

    from src.api.transactions import transactions_bp
    flask_app.register_blueprint(transactions_bp)

    return flask_app

app = config_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
