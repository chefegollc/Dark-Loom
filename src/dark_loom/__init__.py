"""
Dark-Loom: AI Weaver
An advanced AI orchestration and agent framework.
"""

__version__ = "0.1.0"
__author__ = "Dark-Loom Contributors"

from dark_loom.core.agent import Agent
from dark_loom.core.weaver import Weaver
from dark_loom.core.config import Config

__all__ = [
    "Agent",
    "Weaver",
    "Config",
    "__version__",
]
