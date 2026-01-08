"""Configuration management for Dark Loom"""

import os
import yaml
from pathlib import Path
from typing import Dict, Any, Optional
from dotenv import load_dotenv


class Config:
    """Manages configuration for Dark Loom AI Weaver"""

    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize configuration

        Args:
            config_path: Path to YAML configuration file
        """
        load_dotenv()

        self.config_path = config_path
        self.config_data: Dict[str, Any] = {}

        if config_path and os.path.exists(config_path):
            self.load_config(config_path)
        else:
            self._load_defaults()

    def load_config(self, config_path: str):
        """Load configuration from YAML file"""
        with open(config_path, 'r') as f:
            self.config_data = yaml.safe_load(f) or {}

    def _load_defaults(self):
        """Load default configuration"""
        self.config_data = {
            "weaver": {
                "max_threads": int(os.getenv("DARK_LOOM_MAX_THREADS", "4")),
                "timeout": int(os.getenv("DARK_LOOM_TIMEOUT", "300")),
                "verbose": os.getenv("DARK_LOOM_VERBOSE", "false").lower() == "true"
            },
            "tasks": []
        }

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value by key (supports dot notation)"""
        keys = key.split(".")
        value = self.config_data

        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default

        return value if value is not None else default

    def set(self, key: str, value: Any):
        """Set configuration value by key (supports dot notation)"""
        keys = key.split(".")
        config = self.config_data

        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]

        config[keys[-1]] = value

    def save(self, output_path: Optional[str] = None):
        """Save configuration to YAML file"""
        path = output_path or self.config_path
        if not path:
            raise ValueError("No output path specified")

        with open(path, 'w') as f:
            yaml.dump(self.config_data, f, default_flow_style=False)
