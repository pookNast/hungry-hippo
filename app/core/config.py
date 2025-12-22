"""
Configuration settings for Hungry-Hippo application
Environment-based configuration with Pydantic
"""

from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings with validation"""

    # Application
    APP_NAME: str = "Monaco Electric Construction Services"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    # Business Information (sanitized)
    BUSINESS_PHONE: str = "(239) 237-2899"
    BUSINESS_EMAIL: str = "info@monacoelectric.com"
    BUSINESS_LICENSE: str = "EC13009733"
    BUSINESS_ADDRESS: str = "Fort Myers, FL 33912"

    # Service Areas
    SERVICE_AREAS: List[str] = [
        "Fort Myers",
        "Cape Coral",
        "Bonita Springs",
        "Estero"
    ]

    # Performance Targets
    LIGHTHOUSE_TARGET: int = 98
    MAX_JS_SIZE_KB: int = 12
    CLS_TARGET: float = 0.0
    LCP_TARGET_MS: int = 2500

    # Design System (Emergency Modernism)
    EMERGENCY_RED: str = "oklch(0.45 0.19 25)"
    EMERGENCY_RED_HOVER: str = "oklch(0.38 0.21 25)"
    NEUTRAL_50: str = "oklch(0.98 0.01 90)"
    NEUTRAL_900: str = "oklch(0.15 0.01 90)"

    # Touch Targets
    MIN_TOUCH_TARGET_MOBILE: int = 64  # pixels
    MIN_TOUCH_TARGET_DESKTOP: int = 88  # pixels

    # Database (TODO: configure when implementing persistence)
    DATABASE_URL: str = "sqlite:///./hungry_hippo.db"

    # Email (TODO: configure for quote notifications)
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""

    class Config:
        env_file = ".env"
        case_sensitive = True


# Singleton settings instance
settings = Settings()
