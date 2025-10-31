# Dark-Loom Examples

This directory contains example scripts demonstrating various features of Dark-Loom.

## Prerequisites

Before running the examples, make sure you have:

1. Installed Dark-Loom:
   ```bash
   pip install -e .
   ```

2. Set up your API keys:
   ```bash
   export ANTHROPIC_API_KEY=your_key_here
   export OPENAI_API_KEY=your_key_here  # if using OpenAI
   ```

## Examples

### basic_agent.py

Demonstrates basic agent usage including single interactions and multi-turn conversations.

```bash
python examples/basic_agent.py
```

Features:
- Creating an agent
- Single message processing
- Multi-turn conversations with memory
- Clearing conversation history

### multi_agent.py

Shows how to use multiple agents with different personalities using the Weaver.

```bash
python examples/multi_agent.py
```

Features:
- Creating multiple agents
- Configuring different personalities and temperatures
- Registering agents with the Weaver
- Getting responses from different agents

### config_example.py

Demonstrates different configuration methods.

```bash
python examples/config_example.py
```

Features:
- Loading config from environment variables
- Loading config from YAML files
- Programmatic configuration
- Using configuration with agents

## Running Examples

All examples can be run directly:

```bash
cd /path/to/Dark-Loom
python examples/basic_agent.py
```

Or use them as templates for your own projects!

## Creating Your Own Examples

Feel free to create your own examples based on these templates. The basic structure is:

```python
import asyncio
from dark_loom.agents import AnthropicAgent

async def main():
    # Your code here
    pass

if __name__ == "__main__":
    asyncio.run(main())
```

## Troubleshooting

### Missing API Key

If you see "Please set ANTHROPIC_API_KEY environment variable", make sure you've exported your API key:

```bash
export ANTHROPIC_API_KEY=your_actual_key
```

### Import Errors

If you get import errors, make sure Dark-Loom is installed:

```bash
pip install -e .
```

### Module Not Found

Make sure you're running from the correct directory or have the PYTHONPATH set properly.
