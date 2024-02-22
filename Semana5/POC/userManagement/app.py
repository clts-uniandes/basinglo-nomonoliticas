from flask import Flask

from src.config.db import Base
from src.config.db import engine
from src.api.users import users_bp
from src.api.auth import auth_bp

def config_app(flask_app):
    flask_app.config["DEBUG"] = True
    flask_app.config["PROPAGATE_EXCEPTIONS"] = True
    flask_app.config["PRESERVE_CONTEXT_ON_EXCEPTION"] = False
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# init flask app
app = Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)

config_app(app)
Base.metadata.create_all(engine)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
