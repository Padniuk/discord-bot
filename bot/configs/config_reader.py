from pydantic_settings import BaseSettings
from pydantic import SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr
    commands_prefix: str
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()
