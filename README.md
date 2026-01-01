# Interactive Todo Console App

A simple, interactive console-based todo application built with Python.

## Features

- Interactive command-line interface with step-by-step prompts
- Add, view, update, delete, and mark tasks as complete
- In-memory storage (data resets when application closes)
- User-friendly wizard-style interface

## Prerequisites

- Python 3.13 or higher

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Run the application directly with Python

## Usage

Run the application:

```bash
python -m src.main
```

### Available Commands

- `add` - Add a new task
- `view` or `list` - View all tasks
- `update` - Update a task
- `complete` - Mark a task as complete
- `delete` - Delete a task
- `exit` - Exit the application

### Interactive Workflow

The application follows a conversational approach:

1. Enter a command (e.g., "add")
2. The application will prompt you for the required information
3. Follow the prompts to complete your task

Example:
```
Enter command: add
Enter title: Buy groceries
Enter description: Milk, bread, eggs
Task added successfully with ID: 1
```

## Architecture

The application follows the MVC pattern:

- **Model** (`src/models.py`): Task data class
- **Controller** (`src/manager.py`): TaskManager with CRUD logic
- **View** (`src/ui.py`): InteractiveCLI for user interface
- **Entry Point** (`src/main.py`): Application initialization

## Data Storage

All data is stored in memory only. When the application is closed, all tasks are lost.