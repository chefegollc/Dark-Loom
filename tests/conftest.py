"""Pytest configuration and fixtures."""

import pytest

from dark_loom.core.config import Config


@pytest.fixture
def mock_config() -> Config:
    """Create a mock configuration for testing."""
    return Config(
        anthropic_api_key="test_key",
        openai_api_key="test_key",
        default_model="claude-3-5-sonnet-20241022",
        temperature=0.7,
        max_tokens=1000,
        log_level="DEBUG",
    )
