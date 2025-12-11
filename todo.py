import sys
import os

FILE = "todos.txt"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(FILE, "w") as f:
        for t in tasks:
            f.write(t + "\n")

def add(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added:", task)

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

def done(num):
    tasks = load_tasks()
    try:
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print("Completed:", removed)
    except IndexError:
        print("Invalid task number.")

def clear():
    save_tasks([])
    print("All tasks cleared.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 todo.py [add/list/done/clear] <task>")
        exit()

    cmd = sys.argv[1]

    if cmd == "add":
        add(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_tasks()
    elif cmd == "done":
        done(int(sys.argv[2]))
    elif cmd == "clear":
        clear()
    else:
        print("Unknown command")
