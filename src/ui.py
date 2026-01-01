"""
User interface for the Interactive Todo Console App.

This module contains the InteractiveCLI class which provides the
command-line interface for users to interact with the todo application.
"""

from typing import Tuple, List
from .manager import TaskManager
from .models import Task


class InteractiveCLI:
    """
    Interactive command-line interface for the todo application.

    This class provides a conversational interface where users can
    add, view, update, and manage their tasks through step-by-step prompts.
    """

    def __init__(self, task_manager: TaskManager) -> None:
        """
        Initialize the InteractiveCLI with a task manager.

        Args:
            task_manager: The TaskManager instance to use for task operations
        """
        self.task_manager = task_manager

    def prompt_for_add(self) -> Tuple[str, str]:
        """
        Prompt the user for task title and description.

        Returns:
            A tuple containing (title: str, description: str)
        """
        title = input("Enter title: ").strip()
        description = input("Enter description: ").strip()
        return title, description

    def prompt_for_id(self, prompt_text: str = "Enter Task ID: ") -> int:
        """
        Prompt the user for a task ID with custom prompt.

        Args:
            prompt_text: The prompt message to display

        Returns:
            The integer task ID entered by the user

        Raises:
            ValueError: If the user enters invalid input that cannot be converted to an integer
        """
        while True:
            try:
                user_input = input(prompt_text).strip()
                task_id = int(user_input)
                return task_id
            except ValueError:
                print("Please enter a valid number")

    def display_tasks(self, tasks: List[Task]) -> None:
        """
        Display all tasks in a formatted way.

        Args:
            tasks: List of tasks to display
        """
        if not tasks:
            print("No tasks available")
            return

        print("\nYour Tasks:")
        for task in tasks:
            status = "[x]" if task.completed else "[ ]"
            print(f"{status} {task.id}. {task.title}")
            if task.description:
                print(f"     Description: {task.description}")
        print()  # Add blank line after task list

    def show_menu(self) -> None:
        """
        Display the main menu options.
        """
        print("\n" + "="*40)
        print("Interactive Todo App")
        print("="*40)
        print("Available commands:")
        print("  add     - Add a new task")
        print("  view    - View all tasks")
        print("  update  - Update a task")
        print("  complete - Mark a task as complete")
        print("  delete  - Delete a task")
        print("  exit    - Exit the application")
        print("="*40)

    def get_user_choice(self) -> str:
        """
        Get the user's menu choice.

        Returns:
            String representing the user's choice
        """
        choice = input("Enter command: ").strip().lower()
        return choice

    def run(self) -> None:
        """
        Run the main application loop.
        """
        print("Welcome to the Interactive Todo App!")
        print("Type 'help' or '?' for available commands.")

        while True:
            try:
                self.show_menu()
                choice = self.get_user_choice()

                if choice in ['exit', 'quit', 'q']:
                    print("Thank you for using the Interactive Todo App!")
                    break
                elif choice in ['add', 'a']:
                    self._handle_add()
                elif choice in ['view', 'list', 'v', 'l']:
                    self._handle_view()
                elif choice in ['update', 'u']:
                    self._handle_update()
                elif choice in ['complete', 'c']:
                    self._handle_complete()
                elif choice in ['delete', 'd']:
                    self._handle_delete()
                elif choice in ['help', 'h', '?']:
                    continue  # Show menu again
                else:
                    print(f"Unknown command: '{choice}'. Type 'help' for available commands.")
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")

    def _handle_add(self) -> None:
        """Handle the add task command."""
        try:
            title, description = self.prompt_for_add()
            if not title:
                print("Task title cannot be empty. Please try again.")
                return

            task_id = self.task_manager.add_task(title, description)
            print(f"Task added successfully with ID: {task_id}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred while adding task: {e}")

    def _handle_view(self) -> None:
        """Handle the view tasks command."""
        try:
            tasks = self.task_manager.get_all_tasks()
            self.display_tasks(tasks)
        except Exception as e:
            print(f"An error occurred while viewing tasks: {e}")

    def _handle_update(self) -> None:
        """Handle the update task command."""
        try:
            task_id = self.prompt_for_id("Enter Task ID to update: ")
            task = self.task_manager.get_task(task_id)

            if not task:
                print("Invalid ID, try again")
                return

            print(f"Current title: {task.title}")
            new_title = input("Enter new title (or press Enter to keep current): ").strip()
            if new_title == "":
                new_title = task.title

            print(f"Current description: {task.description}")
            new_description = input("Enter new description (or press Enter to keep current): ").strip()
            if new_description == "":
                new_description = task.description

            if self.task_manager.update_task(task_id, new_title, new_description):
                print("Task updated successfully")
            else:
                print("Failed to update task")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred while updating task: {e}")

    def _handle_complete(self) -> None:
        """Handle the complete task command."""
        try:
            task_id = self.prompt_for_id("Enter Task ID to complete: ")
            if self.task_manager.complete_task(task_id):
                print("Task marked as complete")
            else:
                print("Invalid ID, try again")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred while completing task: {e}")

    def _handle_delete(self) -> None:
        """Handle the delete task command."""
        try:
            task_id = self.prompt_for_id("Enter Task ID to delete: ")
            if self.task_manager.delete_task(task_id):
                print("Task deleted successfully")
            else:
                print("Invalid ID, try again")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred while deleting task: {e}")