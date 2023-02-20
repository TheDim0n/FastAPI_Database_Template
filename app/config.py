from pydantic import BaseSettings


class Settings(BaseSettings):
    # database settings
    database_url: str

    # main app settings
    debug: bool = False

    # proxy settings
    root_path: str = ''

    class Config:
        env_file = ".env"
