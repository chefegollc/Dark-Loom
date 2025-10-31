"""Configuration management for Dark-Loom."""

from pathlib import Path
from typing import Any, Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """Main configuration for Dark-Loom."""

    model_config = SettingsConfigDict(
        env_prefix="DARK_LOOM_",
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="allow",
    )

    # API Keys
    anthropic_api_key: Optional[str] = Field(default=None, alias="ANTHROPIC_API_KEY")
    openai_api_key: Optional[str] = Field(default=None, alias="OPENAI_API_KEY")

    # Model Configuration
    default_model: str = Field(default="claude-3-5-sonnet-20241022")
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=4096, gt=0)

    # System Configuration
    log_level: str = Field(default="INFO")
    debug: bool = Field(default=False)
    cache_dir: Path = Field(default=Path.home() / ".cache" / "dark-loom")

    # Weaver Configuration
    max_iterations: int = Field(default=10, gt=0)
    timeout: int = Field(default=300, gt=0)

    def __init__(self, **kwargs: Any) -> None:
        """Initialize configuration."""
        super().__init__(**kwargs)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    @classmethod
    def load(cls, config_file: Optional[Path] = None) -> "Config":
        """Load configuration from file or environment."""
        if config_file and config_file.exists():
            import yaml

            with open(config_file) as f:
                data = yaml.safe_load(f)
            return cls(**data)
        return cls()
