"""
Data models for the Interactive Todo Console App.

This module defines the Task data class used throughout the application.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single todo task with ID, title, description, and completion status.

    Attributes:
        id: Unique identifier for the task
        title: Title of the task (required)
        description: Detailed description of the task (optional)
        completed: Status indicating whether the task is completed (default: False)
    """

    id: int
    title: str
    description: str
    completed: bool = False

    def __post_init__(self) -> None:
        """
        Validate the task after initialization.

        Raises:
            ValueError: If title is empty or None
        """
        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty")