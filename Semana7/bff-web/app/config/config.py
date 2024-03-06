from pydantic_settings import BaseSettings

class BaseConfig(BaseSettings):
    APP_VERSION: str = "1"