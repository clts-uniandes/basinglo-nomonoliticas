from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    users_ms: str
    #transactions_ms: str


settings = Settings()
