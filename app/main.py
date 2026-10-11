"""Minimal to-do API for the fix-gate experiment."""

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()


class TaskCreate(BaseModel):
    """Data sent when adding a task."""

    title: str


# In-memory storage. Resets when the server restarts.
tasks: dict[int, dict] = {}
next_id = 1


def get_task_or_404(task_id: int) -> dict:
    """Return one task, or raise 404 if it does not exist."""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    return tasks[task_id]


@app.get("/")
def index():
    """Show the to-do page."""
    return FileResponse("app/static/index.html")


@app.get("/tasks")
def list_tasks():
    """Return all tasks."""
    return list(tasks.values())


@app.post("/tasks", status_code=201)
def add_task(task: TaskCreate):
    """Add a task. Reject empty or whitespace-only titles."""
    global next_id
    if not task.title.strip():
        raise HTTPException(status_code=400, detail="Title cannot be empty")

    task_id = next_id
    next_id += 1
    tasks[task_id] = {"id": task_id, "title": task.title, "completed": False}
    return tasks[task_id]


@app.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    """Mark one task as completed."""
    task = get_task_or_404(task_id)
    task["completed"] = True
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """Delete one task."""
    get_task_or_404(task_id)
    return tasks.pop(task_id)


app.mount("/static", StaticFiles(directory="app/static"), name="static")
