import os

FILE = "todos.txt"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return [line.strip() for line in f]

def save_tasks(tasks):
    with open(FILE, "w") as f:
        for t in tasks:
            f.write(t + "\n")

def add_task():
    task = input("Enter task: ")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
        print()

def delete_task():
    view_tasks()
    tasks = load_tasks()
    if not tasks:
        return
    num = int(input("Enter task number to delete: "))
    try:
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Task '{removed}' deleted!")
    except:
        print("Invalid number.")

def main_menu():
    while True:
        print("\n==== TODO MENU ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Enter choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()
