from .utils import display_menu, view_tasks, add_task, remove_task

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            task = input("Enter the new task: ")
            add_task(tasks, task)
        elif choice == "3":
            view_tasks(tasks)
            if tasks:
                try:
                    idx = int(input("Enter the number of the task to remove: "))
                    remove_task(tasks, idx)
                except ValueError:
                    print("Invalid input.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
