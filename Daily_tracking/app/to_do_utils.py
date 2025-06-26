def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks, task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(tasks, idx):
    try:
        removed = tasks.pop(idx - 1)
        print(f"Task '{removed}' removed.")
        return True
    except (IndexError, ValueError):
        print("Invalid selection.")
        return False
