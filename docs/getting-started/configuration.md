# Configuration

Dark-Loom provides flexible configuration options through environment variables, YAML files, and programmatic configuration.

## Environment Variables

All configuration can be set via environment variables with the `DARK_LOOM_` prefix:

```bash
# API Keys
export ANTHROPIC_API_KEY=your_key
export OPENAI_API_KEY=your_key

# Model Configuration
export DARK_LOOM_DEFAULT_MODEL=claude-3-5-sonnet-20241022
export DARK_LOOM_TEMPERATURE=0.7
export DARK_LOOM_MAX_TOKENS=4096

# System
export DARK_LOOM_LOG_LEVEL=INFO
export DARK_LOOM_DEBUG=false

# Weaver
export DARK_LOOM_MAX_ITERATIONS=10
export DARK_LOOM_TIMEOUT=300
```

## Configuration File

Create a `dark_loom_config.yaml` file:

```yaml
# Model Configuration
default_model: claude-3-5-sonnet-20241022
temperature: 0.7
max_tokens: 4096

# System Configuration
log_level: INFO
debug: false

# Weaver Configuration
max_iterations: 10
timeout: 300
```

Load the configuration:

```python
from dark_loom import Config

config = Config.load("path/to/dark_loom_config.yaml")
```

## Programmatic Configuration

Configure directly in code:

```python
from dark_loom import Config

config = Config(
    anthropic_api_key="your_key",
    default_model="claude-3-5-sonnet-20241022",
    temperature=0.8,
    max_tokens=2000,
    log_level="DEBUG"
)
```

## Configuration Priority

Configuration is loaded in this order (later overrides earlier):

1. Default values
2. YAML configuration file
3. Environment variables
4. Programmatic configuration

## Available Settings

### API Keys

- `anthropic_api_key`: Anthropic API key
- `openai_api_key`: OpenAI API key

### Model Settings

- `default_model`: Default model to use (default: "claude-3-5-sonnet-20241022")
- `temperature`: Sampling temperature 0.0-2.0 (default: 0.7)
- `max_tokens`: Maximum tokens in response (default: 4096)

### System Settings

- `log_level`: Logging level (default: "INFO")
- `debug`: Enable debug mode (default: false)
- `cache_dir`: Cache directory path (default: ~/.cache/dark-loom)

### Weaver Settings

- `max_iterations`: Maximum weaver iterations (default: 10)
- `timeout`: Timeout in seconds (default: 300)

## CLI Configuration

View current configuration:

```bash
dark-loom config --show
```

Initialize a new project with config files:

```bash
dark-loom init
```

## Best Practices

1. **Use environment variables for secrets**: Keep API keys in `.env` files, never commit them
2. **Use YAML for project settings**: Store non-sensitive configuration in YAML files
3. **Use different configs for environments**: Separate configs for development, testing, production
4. **Version control your config template**: Commit `.env.example` but not `.env`

## Example Setup

```bash
# Initialize project
dark-loom init

# Copy environment template
cp .env.example .env

# Edit .env with your API keys
vim .env

# Customize config
vim dark_loom_config.yaml

# Verify configuration
dark-loom config --show
```
