# API Contracts: Interactive Todo Console App

## TaskManager Contract

### Methods

#### `add_task(title: str, description: str) -> int`
- **Purpose**: Creates a new task with the given title and description
- **Input**:
  - `title`: Non-empty string representing task title
  - `description`: String representing task description (can be empty)
- **Output**: Integer ID of the newly created task
- **Behavior**: Creates a new task with provided details, assigns next available ID, sets completed to False, returns the ID
- **Side Effects**: Task added to in-memory collection

#### `get_task(task_id: int) -> dict`
- **Purpose**: Retrieves a specific task by its ID
- **Input**: `task_id`: Integer representing the unique task identifier
- **Output**: Dictionary containing task details (id, title, description, completed)
- **Behavior**: Returns the task if found, raises exception if not found
- **Error Cases**: Raises exception for invalid/non-existent IDs

#### `get_all_tasks() -> list`
- **Purpose**: Retrieves all tasks in the system
- **Input**: None
- **Output**: List of task dictionaries
- **Behavior**: Returns all tasks in the in-memory collection

#### `update_task(task_id: int, title: str = None, description: str = None) -> bool`
- **Purpose**: Updates an existing task's title and/or description
- **Input**:
  - `task_id`: Integer representing the task to update
  - `title`: Optional new title (if None, current title preserved)
  - `description`: Optional new description (if None, current description preserved)
- **Output**: Boolean indicating success (True) or failure (False)
- **Behavior**: Updates specified fields of existing task, returns True if successful

#### `complete_task(task_id: int) -> bool`
- **Purpose**: Marks a task as completed
- **Input**: `task_id`: Integer representing the task to mark complete
- **Output**: Boolean indicating success (True) or failure (False)
- **Behavior**: Sets the completed field to True for the specified task

#### `delete_task(task_id: int) -> bool`
- **Purpose**: Removes a task from the system
- **Input**: `task_id`: Integer representing the task to delete
- **Output**: Boolean indicating success (True) or failure (False)
- **Behavior**: Removes the task from the in-memory collection

## InteractiveCLI Contract

### Methods

#### `prompt_for_add() -> tuple`
- **Purpose**: Prompts user for task title and description
- **Input**: None (reads from stdin)
- **Output**: Tuple containing (title: str, description: str)
- **Behavior**: Interactively asks user for title and description, validates input

#### `prompt_for_id(prompt_text: str) -> int`
- **Purpose**: Prompts user for a task ID with custom prompt
- **Input**: `prompt_text`: String with the prompt message to show
- **Output**: Integer representing the task ID
- **Behavior**: Asks user for an ID, validates it's a valid integer

#### `display_tasks(tasks: list) -> None`
- **Purpose**: Displays all tasks in a formatted way
- **Input**: `tasks`: List of task dictionaries
- **Output**: None (writes to stdout)
- **Behavior**: Formats and prints tasks with [x] for completed and [ ] for incomplete

#### `show_menu() -> None`
- **Purpose**: Displays the main menu options
- **Input**: None (writes to stdout)
- **Output**: None
- **Behavior**: Shows available options to the user (Add, View, Update, Delete, Exit)

#### `get_user_choice() -> str`
- **Purpose**: Gets the user's menu choice
- **Input**: None (reads from stdin)
- **Output**: String representing the user's choice
- **Behavior**: Prompts user for menu selection and returns it