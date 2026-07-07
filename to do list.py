tasks = []
while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added successfully!")
    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_no = int(input("Enter task number to remove: "))
                if 1 <= task_no <= len(tasks):
                    removed = tasks.pop(task_no - 1)
                    print(f"Task '{removed}' removed successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
