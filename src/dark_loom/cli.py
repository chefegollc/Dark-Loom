"""Command-line interface for Dark-Loom."""

from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel

from dark_loom import __version__
from dark_loom.core.config import Config

app = typer.Typer(
    name="dark-loom",
    help="Dark-Loom: AI Weaver - An advanced AI orchestration framework",
    add_completion=False,
)

console = Console()


def version_callback(value: bool) -> None:
    """Print version and exit."""
    if value:
        console.print(f"Dark-Loom version: {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Show version and exit",
    ),
) -> None:
    """Dark-Loom CLI main entry point."""
    pass


@app.command()
def init(
    path: Path = typer.Argument(Path.cwd(), help="Path to initialize Dark-Loom project"),
    force: bool = typer.Option(False, "--force", "-f", help="Overwrite existing files"),
) -> None:
    """Initialize a new Dark-Loom project."""
    console.print(Panel.fit("🌑 Initializing Dark-Loom project...", border_style="blue"))

    config_file = path / "dark_loom_config.yaml"

    if config_file.exists() and not force:
        console.print(
            f"[yellow]Configuration file already exists at {config_file}[/yellow]",
        )
        console.print("[yellow]Use --force to overwrite[/yellow]")
        raise typer.Exit(1)

    # Create config file
    config_content = """# Dark-Loom Configuration
default_model: claude-3-5-sonnet-20241022
temperature: 0.7
max_tokens: 4096
log_level: INFO
debug: false
max_iterations: 10
timeout: 300
"""

    config_file.write_text(config_content)
    console.print(f"[green]✓[/green] Created configuration file: {config_file}")

    # Create .env template
    env_file = path / ".env.example"
    env_content = """# Dark-Loom Environment Variables
ANTHROPIC_API_KEY=your_anthropic_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
"""
    env_file.write_text(env_content)
    console.print(f"[green]✓[/green] Created environment template: {env_file}")

    console.print("\n[green]✓ Dark-Loom project initialized successfully![/green]")
    console.print("\n[dim]Next steps:[/dim]")
    console.print("  1. Copy .env.example to .env and add your API keys")
    console.print("  2. Customize dark_loom_config.yaml as needed")
    console.print("  3. Start building with Dark-Loom!")


@app.command()
def config(
    show: bool = typer.Option(False, "--show", "-s", help="Show current configuration"),
) -> None:
    """Manage Dark-Loom configuration."""
    if show:
        try:
            cfg = Config.load()
            console.print(Panel.fit("📋 Current Configuration", border_style="blue"))
            console.print(f"Default Model: {cfg.default_model}")
            console.print(f"Temperature: {cfg.temperature}")
            console.print(f"Max Tokens: {cfg.max_tokens}")
            console.print(f"Log Level: {cfg.log_level}")
            console.print(f"Debug: {cfg.debug}")
            console.print(f"Cache Dir: {cfg.cache_dir}")
        except Exception as e:
            console.print(f"[red]Error loading configuration: {e}[/red]")
            raise typer.Exit(1)


@app.command()
def run(
    goal: str = typer.Argument(..., help="Goal to achieve"),
    config_file: Optional[Path] = typer.Option(None, "--config", "-c", help="Config file path"),
) -> None:
    """Run Dark-Loom with a specific goal."""
    console.print(Panel.fit(f"🌑 Dark-Loom: {goal}", border_style="blue"))

    try:
        cfg = Config.load(config_file) if config_file else Config()
        console.print(f"[dim]Using model: {cfg.default_model}[/dim]\n")

        # TODO: Implement actual goal execution
        console.print("[yellow]Goal execution not yet implemented[/yellow]")
        console.print("[dim]This will be implemented in future versions[/dim]")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
