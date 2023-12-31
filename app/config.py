from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings( BaseSettings ):
    port: int = 3000
    

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()