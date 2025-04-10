import os

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()
class Settings(BaseSettings):
    app_name: str = "FastAPI"
    app_version: str = "0.1.0"
    env: str = Field(default="development", env="ENV")

settings = Settings()
