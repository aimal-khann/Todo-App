"""
Task manager for the Interactive Todo Console App.

This module contains the TaskManager class which handles all business logic
for managing tasks, including CRUD operations and in-memory storage.
"""

from typing import Dict, List, Optional
from .models import Task


class TaskManager:
    """
    Manages tasks in memory with CRUD operations.

    This class handles all business logic for task management including
    creating, reading, updating, and deleting tasks. It uses in-memory
    storage as required by the constitution.
    """

    def __init__(self) -> None:
        """Initialize the TaskManager with empty storage."""
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> int:
        """
        Create a new task with the given title and description.

        Args:
            title: Title of the task (required)
            description: Description of the task (optional)

        Returns:
            The ID of the newly created task

        Raises:
            ValueError: If title is empty
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        task_id = self._next_id
        task = Task(id=task_id, title=title.strip(), description=description.strip())
        self._tasks[task_id] = task
        self._next_id += 1
        return task_id

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a specific task by its ID.

        Args:
            task_id: The unique identifier of the task

        Returns:
            The task if found, None otherwise
        """
        return self._tasks.get(task_id)

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks in the system.

        Returns:
            List of all tasks in the system
        """
        return list(self._tasks.values())

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update an existing task's title and/or description.

        Args:
            task_id: The ID of the task to update
            title: New title (if None, current title preserved)
            description: New description (if None, current description preserved)

        Returns:
            True if the task was successfully updated, False otherwise
        """
        if task_id not in self._tasks:
            return False

        task = self._tasks[task_id]

        if title is not None:
            if not title or not title.strip():
                raise ValueError("Task title cannot be empty")
            task.title = title.strip()

        if description is not None:
            task.description = description.strip()

        return True

    def complete_task(self, task_id: int) -> bool:
        """
        Mark a task as completed.

        Args:
            task_id: The ID of the task to mark complete

        Returns:
            True if the task was successfully marked as complete, False otherwise
        """
        if task_id not in self._tasks:
            return False

        self._tasks[task_id].completed = True
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Remove a task from the system.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was successfully deleted, False otherwise
        """
        if task_id not in self._tasks:
            return False

        del self._tasks[task_id]
        return True