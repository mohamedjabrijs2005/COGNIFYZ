import os

TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    try:
        if os.path.exists(TASK_FILE):
            with open(TASK_FILE, "r") as f:
                tasks = [line.strip() for line in f.readlines()]
    except Exception as e:
        print(f"Error loading tasks: {e}")
    return tasks

def save_tasks(tasks):
    try:
        with open(TASK_FILE, "w") as f:
            for task in tasks:
                f.write(task + "\n")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def update_task(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter task number to update: ")) - 1
        if 0 <= idx < len(tasks):
            new_task = input("Enter new task description: ")
            tasks[idx] = new_task
            save_tasks(tasks)
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
            save_tasks(tasks)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Update Task\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()