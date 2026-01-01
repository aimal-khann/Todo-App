# Data Model: Interactive Todo Console App

## Entity: Task

### Fields
- **id**: `int` - Auto-incrementing unique identifier for each task
- **title**: `str` - Title of the task (required, non-empty)
- **description**: `str` - Detailed description of the task (optional, can be empty)
- **completed**: `bool` - Status indicating whether the task is completed (default: False)

### Validation Rules
- **id**: Must be a positive integer, auto-generated and unique within the session
- **title**: Must be a non-empty string with length > 0
- **description**: Can be empty string, no length restrictions
- **completed**: Boolean value only (True/False)

### State Transitions
- **Creation**: `completed` defaults to `False` when a new task is created
- **Completion**: `completed` changes from `False` to `True` when user marks task as complete
- **Uncompletion**: `completed` changes from `True` to `False` when user unmarks task (if supported)
- **Deletion**: Task is removed from the in-memory collection entirely

### Relationships
- No relationships with other entities (standalone entity)

### Example Representation
```python
{
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, bread, eggs, fruits",
    "completed": False
}
```

### Collection Structure
- **In-Memory Storage**: List of Task dictionaries: `[task1, task2, ...]`
- **Access Pattern**: Tasks accessed by ID (integer), requiring lookup in the list
- **Indexing**: For performance, maintain an auxiliary dictionary mapping ID to task for O(1) lookups: `{id: task, ...}`