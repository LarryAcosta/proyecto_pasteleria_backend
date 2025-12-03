from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "Pasteleria API"
    app_env: str = "production"
    debug: bool = False
    database_url: str = "sqlite:///./pasteleria.db"

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()
