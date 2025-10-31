.PHONY: help install install-dev test lint format clean docs

help:
	@echo "Dark-Loom Development Commands"
	@echo "==============================="
	@echo "install        Install package"
	@echo "install-dev    Install package with development dependencies"
	@echo "test          Run tests"
	@echo "test-cov      Run tests with coverage"
	@echo "lint          Run linters"
	@echo "format        Format code"
	@echo "clean         Clean build artifacts"
	@echo "docs          Build documentation"
	@echo "docs-serve    Serve documentation locally"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev,docs]"
	pre-commit install

test:
	pytest tests/

test-cov:
	pytest tests/ --cov=dark_loom --cov-report=html --cov-report=term

lint:
	ruff check src/ tests/
	mypy src/
	black --check src/ tests/

format:
	black src/ tests/
	ruff check --fix src/ tests/

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

docs:
	mkdocs build

docs-serve:
	mkdocs serve
