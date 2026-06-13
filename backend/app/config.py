from pydantic_settings import BaseSettings
from pydantic import field_validator
from typing import Optional


class Settings(BaseSettings):
    # Database: SQLite for local dev; PostgreSQL (Neon/Supabase) for production
    DATABASE_URL: str = "sqlite:///./faraway.db"
    
    # Auth
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    
    # Google OAuth
    GOOGLE_CLIENT_ID: Optional[str] = None
    GOOGLE_CLIENT_SECRET: Optional[str] = None
    
    # Admin (set in production env vars)
    ADMIN_EMAIL: str = "ishumehra1534@gmail.com"
    ADMIN_PASSWORD: str = "Faraway@2026"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    
    # SMTP (for admin OTP emails)
    SMTP_EMAIL: str = "ishumehra1534@gmail.com"
    SMTP_PASSWORD: str = ""  # Gmail App Password - set in .env
    
    # App
    APP_NAME: str = "CollegeSathi"
    FRONTEND_URL: str = "http://localhost:3000"
    
    @field_validator("DATABASE_URL", mode="before")
    @classmethod
    def normalize_database_url(cls, value: str) -> str:
        # Neon/Supabase often provide postgres://; SQLAlchemy expects postgresql://
        if isinstance(value, str) and value.startswith("postgres://"):
            return value.replace("postgres://", "postgresql://", 1)
        return value
    
    class Config:
        env_file = ".env"


settings = Settings()
