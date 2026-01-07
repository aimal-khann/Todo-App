from pydantic_settings import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings(BaseSettings):
    # Database settings - using SQLite for development
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./todo.db")

    # JWT settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-super-secret-key-change-in-production")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

    # Better Auth settings
    BETTER_AUTH_SECRET: str = os.getenv("BETTER_AUTH_SECRET", "your-better-auth-secret-change-in-production")

    # Project settings
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "Todo App Phase II")

    # Other settings
    API_V1_STR: str = "/api/v1"

    class Config:
        env_file = ".env"

settings = Settings()