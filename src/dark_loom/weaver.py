"""Core AI Weaver logic"""

import time
from typing import List, Dict, Any, Callable, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn


class Task:
    """Represents a task in the weaving process"""

    def __init__(self, name: str, func: Callable, args: tuple = (), kwargs: dict = None):
        """
        Initialize a task

        Args:
            name: Task name/description
            func: Function to execute
            args: Positional arguments for the function
            kwargs: Keyword arguments for the function
        """
        self.name = name
        self.func = func
        self.args = args
        self.kwargs = kwargs or {}
        self.result = None
        self.error = None
        self.completed = False

    def execute(self) -> Any:
        """Execute the task"""
        try:
            self.result = self.func(*self.args, **self.kwargs)
            self.completed = True
            return self.result
        except Exception as e:
            self.error = e
            self.completed = True
            raise


class Weaver:
    """AI Weaver - Orchestrates and executes tasks"""

    def __init__(self, config: Optional[Any] = None):
        """
        Initialize the weaver

        Args:
            config: Configuration object
        """
        from .config import Config

        self.config = config or Config()
        self.console = Console()
        self.tasks: List[Task] = []

    def add_task(self, name: str, func: Callable, args: tuple = (), kwargs: dict = None) -> 'Weaver':
        """
        Add a task to the weaver

        Args:
            name: Task name/description
            func: Function to execute
            args: Positional arguments
            kwargs: Keyword arguments

        Returns:
            self for method chaining
        """
        task = Task(name, func, args, kwargs)
        self.tasks.append(task)
        return self

    def run(self, parallel: bool = True) -> List[Any]:
        """
        Execute all tasks

        Args:
            parallel: Whether to run tasks in parallel

        Returns:
            List of task results
        """
        if not self.tasks:
            self.console.print("[yellow]No tasks to execute[/yellow]")
            return []

        max_threads = self.config.get("weaver.max_threads", 4)
        verbose = self.config.get("weaver.verbose", False)

        if verbose:
            self.console.print(f"[cyan]Starting weave with {len(self.tasks)} tasks[/cyan]")

        results = []

        if parallel and len(self.tasks) > 1:
            results = self._run_parallel(max_threads, verbose)
        else:
            results = self._run_sequential(verbose)

        if verbose:
            self.console.print("[green]Weave completed![/green]")

        return results

    def _run_parallel(self, max_threads: int, verbose: bool) -> List[Any]:
        """Run tasks in parallel"""
        results = [None] * len(self.tasks)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=self.console
        ) as progress:

            overall_task = progress.add_task(
                "[cyan]Weaving tasks...",
                total=len(self.tasks)
            )

            with ThreadPoolExecutor(max_workers=max_threads) as executor:
                future_to_task = {
                    executor.submit(task.execute): (idx, task)
                    for idx, task in enumerate(self.tasks)
                }

                for future in as_completed(future_to_task):
                    idx, task = future_to_task[future]
                    try:
                        result = future.result()
                        results[idx] = result
                        if verbose:
                            self.console.print(f"[green]✓[/green] {task.name}")
                    except Exception as e:
                        if verbose:
                            self.console.print(f"[red]✗[/red] {task.name}: {str(e)}")
                        results[idx] = None

                    progress.update(overall_task, advance=1)

        return results

    def _run_sequential(self, verbose: bool) -> List[Any]:
        """Run tasks sequentially"""
        results = []

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console
        ) as progress:

            for task in self.tasks:
                task_progress = progress.add_task(f"[cyan]{task.name}", total=1)

                try:
                    result = task.execute()
                    results.append(result)
                    if verbose:
                        self.console.print(f"[green]✓[/green] {task.name}")
                except Exception as e:
                    if verbose:
                        self.console.print(f"[red]✗[/red] {task.name}: {str(e)}")
                    results.append(None)

                progress.update(task_progress, advance=1)

        return results

    def clear(self):
        """Clear all tasks"""
        self.tasks = []
