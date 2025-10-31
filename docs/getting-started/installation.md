# Installation

## Requirements

- Python 3.9 or higher
- pip or poetry for package management

## Install from PyPI

Once published, you'll be able to install Dark-Loom from PyPI:

```bash
pip install dark-loom
```

## Install from Source

To install the latest development version:

```bash
git clone https://github.com/chefegollc/Dark-Loom.git
cd Dark-Loom
pip install -e .
```

## Development Installation

For development, install with development dependencies:

```bash
pip install -e ".[dev,docs]"
```

Or use the Makefile:

```bash
make install-dev
```

This will also set up pre-commit hooks for code quality.

## Verify Installation

Verify your installation:

```bash
dark-loom --version
```

You should see the version number printed.

## API Keys

Dark-Loom requires API keys for the LLM providers you want to use:

### Anthropic (Claude)

1. Sign up at [Anthropic Console](https://console.anthropic.com/)
2. Create an API key
3. Set the environment variable:

```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

### OpenAI (GPT)

1. Sign up at [OpenAI Platform](https://platform.openai.com/)
2. Create an API key
3. Set the environment variable:

```bash
export OPENAI_API_KEY=your_api_key_here
```

## Configuration

Initialize a new project:

```bash
dark-loom init
```

This creates:
- `dark_loom_config.yaml` - Configuration file
- `.env.example` - Environment template

Copy `.env.example` to `.env` and add your API keys:

```bash
cp .env.example .env
# Edit .env with your favorite editor
```

## Next Steps

- [Quick Start Guide](quickstart.md)
- [Configuration](configuration.md)
