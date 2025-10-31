"""Multi-agent example using the Weaver."""

import asyncio
import os

from dark_loom import Config, Weaver
from dark_loom.agents import AnthropicAgent


async def main() -> None:
    """Run multi-agent example."""
    # Get API key
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Please set ANTHROPIC_API_KEY environment variable")
        return

    # Create configuration
    config = Config(anthropic_api_key=api_key)

    # Create multiple agents with different personalities
    creative_agent = AnthropicAgent(
        name="CreativeAgent",
        api_key=api_key,
        system_prompt="You are a creative writer who thinks outside the box.",
        temperature=1.0,
    )

    analytical_agent = AnthropicAgent(
        name="AnalyticalAgent",
        api_key=api_key,
        system_prompt="You are a logical analyst who breaks down problems systematically.",
        temperature=0.3,
    )

    # Create weaver
    weaver = Weaver(config)
    weaver.register_agent(creative_agent)
    weaver.register_agent(analytical_agent)

    # List registered agents
    print("Registered agents:", weaver.list_agents())
    print()

    # Get responses from both agents on the same topic
    topic = "Explain the concept of artificial intelligence"

    print(f"Topic: {topic}\n")

    print("=== Creative Agent ===")
    creative_response = await creative_agent.process(topic)
    print(creative_response.content)
    print()

    print("=== Analytical Agent ===")
    analytical_response = await analytical_agent.process(topic)
    print(analytical_response.content)
    print()


if __name__ == "__main__":
    asyncio.run(main())
