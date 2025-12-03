from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # Valores por defecto para que NO falle si no hay variables de entorno
    app_name: str = "Pasteleria API"
    app_env: str = "production"
    debug: bool = False
    database_url: str = "sqlite:///./pasteleria.db"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings():
    return Settings()
