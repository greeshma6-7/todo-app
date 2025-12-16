from flask import Flask, request, redirect, url_for, render_template_string
import os

app = Flask(__name__)
FILE = "todos.txt"

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Todo App</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        h1 { color: #333; }
        input { padding: 6px; }
        button { padding: 6px; }
        ul { list-style: none; padding: 0; }
        li { margin: 6px 0; }
    </style>
</head>
<body>
    <h1>Todo Application</h1>

    <form method="POST" action="/add">
        <input type="text" name="task" placeholder="Enter task" required>
        <button type="submit">Add Task</button>
    </form>

    <h2>Your Tasks</h2>
    <ul>
        {% for i, task in tasks %}
            <li>
                {{ i + 1 }}. {{ task }}
                <a href="/delete/{{ i }}">❌</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
"""

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

def save_tasks(tasks):
    with open(FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

@app.route("/")
def index():
    tasks = load_tasks()
    return render_template_string(HTML_PAGE, tasks=list(enumerate(tasks)))

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        tasks = load_tasks()
        tasks.append(task)
        save_tasks(tasks)
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
