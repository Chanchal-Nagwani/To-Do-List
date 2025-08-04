# Simple To-Do List Program

todo_list = []

def show_menu():
    print("\n==== TO-DO LIST MENU ====")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def show_tasks():
    if not todo_list:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f"Task '{task}' added!")

def remove_task():
    show_tasks()
    try:
        task_no = int(input("Enter the task number to remove: "))
        if 1 <= task_no <= len(todo_list):
            removed = todo_list.pop(task_no - 1)
            print(f"Task '{removed}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-4.")
