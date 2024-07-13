from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    DATABASE: str
    USER: str
    HOST: str
    PASSWORD: str
    API_ID: int
    API_HASH: str
    BOT_TOKEN: str

settings = Settings()
