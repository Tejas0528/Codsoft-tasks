tasks = []

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid choice. Please try again.")

main()