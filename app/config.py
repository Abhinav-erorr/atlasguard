"""Application configuration."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings loaded from environment variables."""

    app_name: str = "AtlasGuard"
    environment: str = "development"
    debug: bool = False

    model_config = SettingsConfigDict(
        env_prefix="ATLASGUARD_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return the cached application settings."""

    return Settings()
