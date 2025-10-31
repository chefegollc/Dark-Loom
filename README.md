# 🌑 Dark-Loom: AI Weaver

[![CI](https://github.com/chefegollc/Dark-Loom/workflows/CI/badge.svg)](https://github.com/chefegollc/Dark-Loom/actions)
[![Documentation](https://github.com/chefegollc/Dark-Loom/workflows/Documentation/badge.svg)](https://github.com/chefegollc/Dark-Loom/actions)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An advanced AI orchestration and agent framework designed to weave together multiple AI agents to accomplish complex tasks.

## ✨ Features

- 🤖 **Multi-Agent System**: Create and coordinate multiple AI agents with different capabilities
- 🔌 **Provider Agnostic**: Support for Anthropic Claude, OpenAI GPT, and extensible to other providers
- 🕸️ **Weaver Orchestration**: Sophisticated orchestration engine for coordinating agent workflows
- 🛠️ **Tool Integration**: Easily extend agents with custom tools and capabilities
- ⚙️ **Flexible Configuration**: Environment variables, YAML files, or programmatic configuration
- 📝 **Type Safe**: Full type hints and MyPy support
- 🧪 **Well Tested**: Comprehensive test suite with pytest
- 📚 **Rich Documentation**: Detailed docs with examples

## 🚀 Quick Start

### Installation

```bash
pip install dark-loom
```

Or install from source:

```bash
git clone https://github.com/chefegollc/Dark-Loom.git
cd Dark-Loom
pip install -e .
```

### Basic Usage

```python
import asyncio
from dark_loom.agents import AnthropicAgent

async def main():
    agent = AnthropicAgent(
        name="Assistant",
        api_key="your-api-key",
        system_prompt="You are a helpful assistant"
    )

    response = await agent.process("Hello! How can you help me?")
    print(response.content)

asyncio.run(main())
```

### Multi-Agent Orchestration

```python
from dark_loom import Weaver, Config
from dark_loom.agents import AnthropicAgent, OpenAIAgent

# Create agents
claude = AnthropicAgent(name="Claude", api_key="...")
gpt = OpenAIAgent(name="GPT", api_key="...")

# Orchestrate with Weaver
weaver = Weaver(Config())
weaver.register_agent(claude)
weaver.register_agent(gpt)

# Execute complex goals
results = await weaver.weave("Solve this complex problem")
```

## 📖 Documentation

Full documentation is available at [GitHub Pages](https://chefegollc.github.io/Dark-Loom/) (coming soon).

### Quick Links

- [Installation Guide](docs/getting-started/installation.md)
- [Quick Start Tutorial](docs/getting-started/quickstart.md)
- [Configuration](docs/getting-started/configuration.md)
- [Examples](examples/)

## 🏗️ Project Structure

```
Dark-Loom/
├── src/dark_loom/          # Main package
│   ├── core/               # Core abstractions
│   │   ├── agent.py        # Base agent class
│   │   ├── config.py       # Configuration management
│   │   └── weaver.py       # Orchestration engine
│   ├── agents/             # Provider implementations
│   │   ├── anthropic_agent.py
│   │   └── openai_agent.py
│   ├── tools/              # Agent tools
│   ├── utils/              # Utilities
│   └── cli.py              # Command-line interface
├── tests/                  # Test suite
├── docs/                   # Documentation
├── examples/               # Example scripts
└── configs/                # Configuration files
```

## 🔧 Configuration

Dark-Loom can be configured in multiple ways:

### Environment Variables

```bash
export ANTHROPIC_API_KEY=your_key
export OPENAI_API_KEY=your_key
export DARK_LOOM_DEFAULT_MODEL=claude-3-5-sonnet-20241022
```

### YAML Configuration

```yaml
# dark_loom_config.yaml
default_model: claude-3-5-sonnet-20241022
temperature: 0.7
max_tokens: 4096
```

### Programmatic

```python
from dark_loom import Config

config = Config(
    default_model="claude-3-5-sonnet-20241022",
    temperature=0.7,
    max_tokens=4096
)
```

## 💻 CLI

Dark-Loom includes a command-line interface:

```bash
# Initialize a new project
dark-loom init

# Show configuration
dark-loom config --show

# Run with a goal
dark-loom run "Your goal here"

# Show version
dark-loom --version
```

## 🧪 Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/chefegollc/Dark-Loom.git
cd Dark-Loom

# Install with development dependencies
make install-dev

# Run tests
make test

# Run linters
make lint

# Format code
make format
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=dark_loom --cov-report=html

# Or use make
make test-cov
```

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Requirements

- Python 3.9+
- Dependencies listed in `requirements.txt`

## 🔒 Security

- Never commit API keys or secrets
- Use environment variables for sensitive data
- Review the [security policy](SECURITY.md) (coming soon)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Anthropic Claude](https://www.anthropic.com/) and [OpenAI GPT](https://openai.com/)
- Powered by [Pydantic](https://pydantic.dev/) for data validation
- CLI built with [Typer](https://typer.tiangolo.com/) and [Rich](https://rich.readthedocs.io/)

## 📞 Contact & Support

- 📫 Issues: [GitHub Issues](https://github.com/chefegollc/Dark-Loom/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/chefegollc/Dark-Loom/discussions)

## 🗺️ Roadmap

- [ ] Additional LLM provider support
- [ ] Tool/function calling support
- [ ] Streaming responses
- [ ] Advanced orchestration patterns
- [ ] Vector database integration
- [ ] Memory systems
- [ ] Web interface
- [ ] More examples and tutorials

## ⭐ Star History

If you find Dark-Loom useful, please consider giving it a star!

---

**Dark-Loom** - Weaving intelligence, one thread at a time. 🧵✨
