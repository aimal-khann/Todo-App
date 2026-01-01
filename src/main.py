"""
Entry point for the Interactive Todo Console App.

This module initializes the application components and starts the main loop.
"""

from .manager import TaskManager
from .ui import InteractiveCLI


def main() -> None:
    """
    Main entry point for the application.

    Initializes the TaskManager and InteractiveCLI, then starts the application loop.
    """
    # Initialize the task manager
    task_manager = TaskManager()

    # Initialize the user interface
    cli = InteractiveCLI(task_manager)

    # Start the application
    cli.run()


if __name__ == "__main__":
    main()