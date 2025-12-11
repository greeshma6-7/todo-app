if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python todo.py [add/list/done] <task>")
        exit()

    cmd = sys.argv[1]

    if cmd == "add":
        add(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_tasks()
    elif cmd == "done":
        done(int(sys.argv[2]))
    elif cmd == "clear":
        tasks.clear()
        print("All tasks cleared.")
    else:
        print("Unknown command")
