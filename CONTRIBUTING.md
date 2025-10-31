# Contributing to Dark-Loom

Thank you for your interest in contributing to Dark-Loom! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/Dark-Loom.git
   cd Dark-Loom
   ```
3. Install development dependencies:
   ```bash
   make install-dev
   ```

## Development Workflow

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and ensure they follow the project's coding standards

3. Run tests:
   ```bash
   make test
   ```

4. Run linters and formatters:
   ```bash
   make lint
   make format
   ```

5. Commit your changes:
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

6. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

7. Open a Pull Request

## Code Style

We use:
- **Black** for code formatting
- **Ruff** for linting
- **MyPy** for type checking

Run all checks before committing:
```bash
make lint
make format
```

## Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Aim for high test coverage

```bash
# Run tests
make test

# Run tests with coverage
make test-cov
```

## Documentation

- Update documentation for new features
- Use Google-style docstrings
- Update README.md if needed

```bash
# Build docs
make docs

# Serve docs locally
make docs-serve
```

## Pre-commit Hooks

We use pre-commit hooks to ensure code quality. They're installed automatically with `make install-dev`.

To run manually:
```bash
pre-commit run --all-files
```

## Pull Request Guidelines

1. **Title**: Use a clear, descriptive title
2. **Description**: Explain what changes you made and why
3. **Tests**: Include tests for new functionality
4. **Documentation**: Update docs as needed
5. **Commits**: Keep commits focused and well-described

## Reporting Bugs

When reporting bugs, please include:
- Python version
- Operating system
- Steps to reproduce
- Expected behavior
- Actual behavior
- Error messages/stack traces

## Feature Requests

We welcome feature requests! Please:
- Check if the feature already exists
- Clearly describe the feature and its use case
- Explain why it would be beneficial

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help create a welcoming environment

## Questions?

Feel free to open an issue for questions or discussions.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
