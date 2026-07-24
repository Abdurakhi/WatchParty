from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Global application settings.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # --------------------------------------------------
    # Application
    # --------------------------------------------------

    APP_NAME: str = Field(default="WatchParty")
    APP_VERSION: str = Field(default="0.1.0")
    DEBUG: bool = Field(default=True)
    ENVIRONMENT: str = Field(default="development")

    API_PREFIX: str = Field(default="/api/v1")

    # --------------------------------------------------
    # Server
    # --------------------------------------------------

    HOST: str = Field(default="0.0.0.0")
    PORT: int = Field(default=8000)

    # --------------------------------------------------
    # Security
    # --------------------------------------------------

    SECRET_KEY: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30)

    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(default=30)

    JWT_ALGORITHM: str = Field(default="HS256")

    # --------------------------------------------------
    # PostgreSQL
    # --------------------------------------------------

    POSTGRES_HOST: str

    POSTGRES_PORT: int

    POSTGRES_DB: str

    POSTGRES_USER: str

    POSTGRES_PASSWORD: str

    # --------------------------------------------------
    # Redis
    # --------------------------------------------------

    REDIS_HOST: str

    REDIS_PORT: int

    REDIS_PASSWORD: str = Field(default="")

    # --------------------------------------------------
    # Browser Service
    # --------------------------------------------------

    BROWSER_SERVICE_HOST: str

    BROWSER_SERVICE_PORT: int

    # --------------------------------------------------
    # WebSocket
    # --------------------------------------------------

    WS_HEARTBEAT_INTERVAL: int = Field(default=30)

    WS_MAX_CONNECTIONS: int = Field(default=5000)

    # --------------------------------------------------
    # CORS
    # --------------------------------------------------

    CORS_ORIGINS: list[str] = Field(
        default=[
            "http://localhost:5173",
            "http://127.0.0.1:5173",
        ]
    )

    # --------------------------------------------------
    # Database URL
    # --------------------------------------------------

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )

    # --------------------------------------------------
    # Redis URL
    # --------------------------------------------------

    @property
    def REDIS_URL(self) -> str:

        if self.REDIS_PASSWORD:
            return (
                f"redis://:{self.REDIS_PASSWORD}"
                f"@{self.REDIS_HOST}:{self.REDIS_PORT}"
            )

        return (
            f"redis://"
            f"{self.REDIS_HOST}:{self.REDIS_PORT}"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
