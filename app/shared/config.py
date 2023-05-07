from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    # database settings
    db_url: str = PostgresDsn
    db_scheme: str = 'public'

    # main app settings
    debug: bool = False

    # proxy settings
    root_path: str = ''

    class Config:
        env_file = ".env"
