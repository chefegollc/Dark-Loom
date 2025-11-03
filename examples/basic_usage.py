#!/usr/bin/env python3
"""
Basic usage example for Dark Loom AI Weaver
"""

import time
from dark_loom import Weaver, Config


def task_a():
    """Simulate some AI processing"""
    time.sleep(1)
    return "Task A: Model initialized"


def task_b(model_name):
    """Process data with a model"""
    time.sleep(1.5)
    return f"Task B: Processed data with {model_name}"


def task_c():
    """Generate output"""
    time.sleep(0.5)
    return "Task C: Output generated"


def main():
    # Create a configuration
    config = Config()
    config.set("weaver.max_threads", 3)
    config.set("weaver.verbose", True)

    # Create a weaver instance
    weaver = Weaver(config)

    # Add tasks
    weaver.add_task("Initialize Model", task_a)
    weaver.add_task("Process Data", task_b, args=("GPT-4",))
    weaver.add_task("Generate Output", task_c)

    # Run tasks in parallel
    print("Running tasks in parallel...")
    results = weaver.run(parallel=True)

    print("\nResults:")
    for i, result in enumerate(results, 1):
        print(f"  {i}. {result}")


if __name__ == "__main__":
    main()
