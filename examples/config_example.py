"""Configuration example."""

import asyncio
import os
from pathlib import Path

from dark_loom import Config
from dark_loom.agents import AnthropicAgent


async def main() -> None:
    """Run configuration example."""
    # Method 1: Load from environment variables
    print("=== Method 1: Environment Variables ===")
    config1 = Config()
    print(f"Default Model: {config1.default_model}")
    print(f"Temperature: {config1.temperature}")
    print(f"Max Tokens: {config1.max_tokens}")
    print()

    # Method 2: Load from YAML file (if exists)
    print("=== Method 2: YAML File ===")
    config_file = Path("dark_loom_config.yaml")
    if config_file.exists():
        config2 = Config.load(config_file)
        print(f"Loaded from: {config_file}")
        print(f"Default Model: {config2.default_model}")
    else:
        print(f"Config file not found at {config_file}")
    print()

    # Method 3: Programmatic configuration
    print("=== Method 3: Programmatic ===")
    config3 = Config(
        anthropic_api_key=os.getenv("ANTHROPIC_API_KEY", "not-set"),
        default_model="claude-3-5-sonnet-20241022",
        temperature=0.8,
        max_tokens=2000,
        log_level="DEBUG",
    )
    print(f"Default Model: {config3.default_model}")
    print(f"Temperature: {config3.temperature}")
    print(f"Max Tokens: {config3.max_tokens}")
    print()

    # Use configuration with agent
    if os.getenv("ANTHROPIC_API_KEY"):
        print("=== Using Config with Agent ===")
        agent = AnthropicAgent(
            name="ConfiguredAgent",
            api_key=config3.anthropic_api_key,
            model=config3.default_model,
            temperature=config3.temperature,
            max_tokens=config3.max_tokens,
        )

        response = await agent.process("Say hello!")
        print(f"Agent response: {response.content}")


if __name__ == "__main__":
    asyncio.run(main())
