# Quickstart Guide: Interactive Todo Console App

## Getting Started

### Prerequisites
- Python 3.13+ installed
- UV package manager installed

### Setup
1. Clone the repository
2. Navigate to the project directory
3. Install dependencies: `uv sync` (or `pip install -r requirements.txt`)

### Running the Application
1. Execute: `python src/main.py`
2. The application will start with a menu showing available options
3. Follow the interactive prompts to add, view, update, complete, or delete tasks

## Basic Usage

### Adding a Task
1. Select "Add" from the main menu
2. Enter the task title when prompted
3. Enter the task description when prompted
4. The task will be added to your list

### Viewing Tasks
1. Select "View" from the main menu
2. All tasks will be displayed with [ ] for incomplete and [x] for completed tasks

### Updating a Task
1. Select "Update" from the main menu
2. Enter the Task ID when prompted
3. Enter the new title when prompted
4. Enter the new description when prompted

### Completing a Task
1. Select "Complete" from the main menu
2. Enter the Task ID when prompted
3. The task will be marked as completed

### Deleting a Task
1. Select "Delete" from the main menu
2. Enter the Task ID when prompted
3. The task will be removed from your list

## Error Handling
- If you enter an invalid Task ID, the application will show "Invalid ID, try again" and prompt you again
- The application will never crash due to invalid input
- Empty titles will be rejected with a prompt to enter a valid title

## Architecture Overview
The application follows the MVC pattern:
- **Model (src/models.py)**: Task data class
- **Controller (src/manager.py)**: TaskManager with CRUD operations
- **View (src/ui.py)**: InteractiveCLI for user interface
- **Entry Point (src/main.py)**: Orchestrates the components