# Task Manager CRUD Application with File Persistence

This project is a simple Python CRUD (Create, Read, Update, Delete) application for managing tasks, implemented in a Jupyter Notebook. It demonstrates how to store and manage tasks persistently using file I/O.

## Features

- **Add Task:** Add a new task to your list.
- **View Tasks:** Display all saved tasks.
- **Update Task:** Edit an existing task.
- **Delete Task:** Remove a task from your list.
- **Persistent Storage:** All tasks are saved in `tasks.txt` and loaded automatically.
- **Error Handling:** Handles file read/write errors gracefully.

## How It Works

- Tasks are stored as plain text, one per line, in `tasks.txt`.
- The notebook loads tasks from the file at startup and saves changes after every add, update, or delete operation.
- All file operations are wrapped in try/except blocks for safety.

## How to Use

1. Open the notebook `CRUD Application NoteBook.ipynb` in Jupyter Notebook or JupyterLab.
2. Run the cells in order to load the functions.
3. Use the provided example cells to add, view, update, or delete tasks.
4. Check the `tasks.txt` file in the same directory to see your saved tasks.

## Example Usage

```python
# Load tasks
tasks = load_tasks()
view_tasks(tasks)

# Add a task
add_task(tasks, "Buy groceries")
view_tasks(tasks)

# Update a task
update_task(tasks, 0, "Buy groceries and cook dinner")
view_tasks(tasks)

# Delete a task
delete_task(tasks, 0)
view_tasks(tasks)
```

## File Structure

- `CRUD Application NoteBook.ipynb` — Main Jupyter Notebook with all code and instructions.
- `tasks.txt` — Text file where tasks are stored (created automatically).

---

**Note:**  
If `tasks.txt` does not exist, it will be created automatically when you add or save