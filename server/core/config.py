from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):

    database_user: str
    database_password: str
    database_name: str
    database_host: str

    model_config = SettingsConfigDict(env_file=".env."+os.getenv("ENV_MODE"))

settings = Settings()