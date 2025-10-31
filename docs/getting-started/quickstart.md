# Quick Start Guide

This guide will help you get started with Dark-Loom quickly.

## Setup

First, make sure you have installed Dark-Loom and configured your API keys (see [Installation](installation.md)).

## Your First Agent

Create a simple agent:

```python
import asyncio
from dark_loom.agents import AnthropicAgent

async def main():
    # Create an agent
    agent = AnthropicAgent(
        name="MyAssistant",
        api_key="your-anthropic-api-key",
        model="claude-3-5-sonnet-20241022"
    )

    # Send a message
    response = await agent.process("What is the capital of France?")

    # Print the response
    print(response.content)

# Run the async function
asyncio.run(main())
```

## Using Configuration

Use the configuration system for better management:

```python
import asyncio
from dark_loom import Config
from dark_loom.agents import AnthropicAgent

async def main():
    # Load configuration
    config = Config.load()

    # Create agent with config
    agent = AnthropicAgent(
        name="MyAssistant",
        api_key=config.anthropic_api_key,
        model=config.default_model,
        temperature=config.temperature
    )

    response = await agent.process("Tell me a joke")
    print(response.content)

asyncio.run(main())
```

## Conversation History

Agents maintain conversation history automatically:

```python
import asyncio
from dark_loom.agents import AnthropicAgent

async def main():
    agent = AnthropicAgent(
        name="Assistant",
        api_key="your-api-key"
    )

    # First message
    response1 = await agent.process("My name is Alice")
    print(response1.content)

    # Second message - agent remembers context
    response2 = await agent.process("What's my name?")
    print(response2.content)

    # View history
    history = agent.get_history()
    for msg in history:
        print(f"{msg.role}: {msg.content}")

asyncio.run(main())
```

## Using the Weaver

Coordinate multiple agents:

```python
import asyncio
from dark_loom import Config, Weaver
from dark_loom.agents import AnthropicAgent, OpenAIAgent

async def main():
    config = Config.load()

    # Create multiple agents
    claude = AnthropicAgent(
        name="Claude",
        api_key=config.anthropic_api_key
    )

    gpt = OpenAIAgent(
        name="GPT",
        api_key=config.openai_api_key
    )

    # Create weaver
    weaver = Weaver(config)
    weaver.register_agent(claude)
    weaver.register_agent(gpt)

    # Execute a goal
    results = await weaver.weave(
        goal="Explain quantum computing in simple terms",
        max_iterations=3
    )

    for result in results:
        print(result.content)

asyncio.run(main())
```

## Next Steps

- Learn about [Configuration](configuration.md)
- Explore [Core Concepts](../concepts/agents.md)
- See more [Examples](../examples/basic.md)
