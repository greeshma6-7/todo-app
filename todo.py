tasks = []

def add(task):
    tasks.append(task)
    print("Task added:", task)

def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

def done(num):
    try:
        removed = tasks.pop(num - 1)
        print("Completed:", removed)
    except IndexError:
        print("Invalid task number.")

def clear():
    tasks.clear()
    print("All tasks cleared.")

if __name__ == "__main__":
    import sys
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
