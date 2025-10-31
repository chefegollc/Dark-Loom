"""Basic agent example."""

import asyncio
import os

from dark_loom.agents import AnthropicAgent


async def main() -> None:
    """Run basic agent example."""
    # Get API key from environment
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Please set ANTHROPIC_API_KEY environment variable")
        return

    # Create agent
    agent = AnthropicAgent(
        name="BasicAssistant",
        api_key=api_key,
        model="claude-3-5-sonnet-20241022",
        system_prompt="You are a helpful and friendly assistant.",
    )

    # Single interaction
    print("=== Single Interaction ===")
    response = await agent.process("What is the capital of France?")
    print(f"Agent: {response.content}\n")

    # Clear history for new conversation
    agent.clear_history()

    # Multi-turn conversation
    print("=== Multi-turn Conversation ===")

    messages = [
        "My name is Alice and I love programming.",
        "What's my name?",
        "What do I love?",
    ]

    for msg in messages:
        print(f"User: {msg}")
        response = await agent.process(msg)
        print(f"Agent: {response.content}\n")


if __name__ == "__main__":
    asyncio.run(main())
