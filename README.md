# Dark Loom 🕸️

**AI Weaver** - Orchestrate and weave AI operations together

Dark Loom is a Python framework for orchestrating and executing AI tasks in parallel or sequential workflows. It provides a clean, intuitive API for managing complex AI pipelines with built-in progress tracking and error handling.

## Features

- **Parallel & Sequential Execution**: Run tasks concurrently or step-by-step
- **Progress Tracking**: Beautiful console output with real-time progress
- **Configuration Management**: YAML-based config with environment variable support
- **Error Handling**: Robust error capture and reporting
- **CLI Interface**: Command-line tool for quick execution
- **Extensible**: Easy to add custom tasks and workflows

## Installation

```bash
# Clone the repository
git clone https://github.com/chefegollc/Dark-Loom.git
cd Dark-Loom

# Install dependencies
pip install -r requirements.txt

# Install Dark Loom
pip install -e .
```

## Quick Start

### Using the CLI

```bash
# Run with default settings
dark-loom run

# Run with custom config
dark-loom run --config examples/config.yaml

# Run in sequential mode with verbose output
dark-loom run --sequential --verbose

# Initialize a new configuration file
dark-loom init my-config.yaml

# Display information
dark-loom info
```

### Using the Python API

```python
from dark_loom import Weaver, Config

# Create a weaver
weaver = Weaver()

# Add tasks
weaver.add_task("Initialize Model", initialize_model)
weaver.add_task("Process Data", process_data, args=(data,))
weaver.add_task("Generate Output", generate_output)

# Run tasks in parallel
results = weaver.run(parallel=True)
```

See `examples/basic_usage.py` for a complete example.

## Configuration

Dark Loom can be configured via YAML files or environment variables:

### YAML Configuration

```yaml
weaver:
  max_threads: 4
  timeout: 300
  verbose: true

tasks:
  - name: task_1
    description: "First task"
    enabled: true
```

### Environment Variables

```bash
DARK_LOOM_MAX_THREADS=4
DARK_LOOM_TIMEOUT=300
DARK_LOOM_VERBOSE=true
```

## Project Structure

```
Dark-Loom/
├── src/
│   └── dark_loom/
│       ├── __init__.py      # Package initialization
│       ├── cli.py           # Command-line interface
│       ├── config.py        # Configuration management
│       └── weaver.py        # Core weaving logic
├── examples/
│   ├── basic_usage.py       # Basic usage example
│   └── config.yaml          # Example configuration
├── tests/                   # Unit tests (coming soon)
├── requirements.txt         # Python dependencies
├── setup.py                 # Package setup
└── README.md               # This file
```

## Development

```bash
# Install in development mode
pip install -e .

# Run tests (coming soon)
pytest tests/
```

## Use Cases

- **AI Pipeline Orchestration**: Chain multiple AI models together
- **Batch Processing**: Process large datasets in parallel
- **Multi-Model Inference**: Run multiple models concurrently
- **Data Processing**: ETL pipelines with AI components
- **Workflow Automation**: Automate complex AI workflows

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

MIT License - see LICENSE file for details

## About

Dark Loom is an AI orchestration framework designed to simplify the execution of complex AI workflows. Whether you're running multiple models in parallel or chaining tasks together, Dark Loom provides the tools you need to weave your AI operations seamlessly.
