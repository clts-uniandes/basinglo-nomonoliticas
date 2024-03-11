from flask import Blueprint

def create_blueprint(identificador: str, url_prefix: str):
    return Blueprint(identificador, __name__, url_prefix=url_prefix)