"""Command-line interface for Dark Loom"""

import click
import time
from pathlib import Path
from rich.console import Console

from .config import Config
from .weaver import Weaver


console = Console()


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """
    Dark Loom - AI Weaver

    Orchestrate and weave AI operations together.
    """
    pass


@cli.command()
@click.option(
    '--config', '-c',
    type=click.Path(exists=True),
    help='Path to configuration file (YAML)'
)
@click.option(
    '--parallel/--sequential',
    default=True,
    help='Run tasks in parallel or sequential mode'
)
@click.option(
    '--verbose', '-v',
    is_flag=True,
    help='Enable verbose output'
)
def run(config, parallel, verbose):
    """
    Run the AI weaver with configured tasks
    """
    console.print("[bold cyan]Dark Loom - AI Weaver[/bold cyan]")
    console.print()

    # Load configuration
    cfg = Config(config)
    if verbose:
        cfg.set("weaver.verbose", True)

    # Create weaver instance
    weaver = Weaver(cfg)

    # Example tasks - these would normally come from config
    # For demonstration, we'll add some sample tasks
    def example_task_1():
        time.sleep(1)
        return "Task 1 completed"

    def example_task_2():
        time.sleep(1.5)
        return "Task 2 completed"

    def example_task_3():
        time.sleep(0.5)
        return "Task 3 completed"

    weaver.add_task("Initialize AI model", example_task_1)
    weaver.add_task("Process data pipeline", example_task_2)
    weaver.add_task("Generate output", example_task_3)

    # Run the weaver
    console.print("[yellow]Starting weave...[/yellow]")
    results = weaver.run(parallel=parallel)

    console.print()
    console.print(f"[green]Completed {len(results)} tasks![/green]")

    if verbose:
        for i, result in enumerate(results):
            console.print(f"  Task {i+1}: {result}")


@cli.command()
@click.argument('output', type=click.Path())
def init(output):
    """
    Initialize a new Dark Loom configuration file
    """
    config = Config()
    config.set("weaver.max_threads", 4)
    config.set("weaver.timeout", 300)
    config.set("weaver.verbose", False)
    config.set("tasks", [
        {
            "name": "example_task",
            "description": "An example task",
            "enabled": True
        }
    ])

    config.save(output)
    console.print(f"[green]Configuration file created at: {output}[/green]")


@cli.command()
def info():
    """
    Display information about Dark Loom
    """
    console.print("[bold cyan]Dark Loom - AI Weaver[/bold cyan]")
    console.print("Version: 0.1.0")
    console.print()
    console.print("An orchestration framework for weaving AI operations together.")
    console.print()
    console.print("[yellow]Features:[/yellow]")
    console.print("  • Parallel and sequential task execution")
    console.print("  • Configuration management via YAML")
    console.print("  • Rich console output with progress tracking")
    console.print("  • Extensible task framework")


def main():
    """Main entry point"""
    cli()


if __name__ == "__main__":
    main()
