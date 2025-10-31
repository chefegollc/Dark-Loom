"""Tests for configuration module."""

import pytest

from dark_loom.core.config import Config


def test_config_defaults() -> None:
    """Test default configuration values."""
    config = Config(anthropic_api_key="test")
    assert config.default_model == "claude-3-5-sonnet-20241022"
    assert config.temperature == 0.7
    assert config.max_tokens == 4096
    assert config.log_level == "INFO"
    assert config.debug is False


def test_config_custom_values() -> None:
    """Test custom configuration values."""
    config = Config(
        anthropic_api_key="test_key",
        default_model="gpt-4",
        temperature=1.0,
        max_tokens=2000,
    )
    assert config.default_model == "gpt-4"
    assert config.temperature == 1.0
    assert config.max_tokens == 2000


def test_config_cache_dir_creation(tmp_path: pytest.TempPathFactory) -> None:
    """Test cache directory is created."""
    cache_dir = tmp_path / "cache"
    config = Config(anthropic_api_key="test", cache_dir=cache_dir)
    assert config.cache_dir.exists()
