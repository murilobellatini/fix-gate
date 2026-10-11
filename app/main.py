from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()


class TaskCreate(BaseModel):
    title: str


tasks: dict[int, dict] = {}
next_id = 1


@app.get("/")
def index():
    return FileResponse("app/static/index.html")


@app.get("/tasks")
def list_tasks():
    return list(tasks.values())


@app.post("/tasks", status_code=201)
def add_task(task: TaskCreate):
    global next_id
    if not task.title.strip():
        raise HTTPException(status_code=400, detail="Title cannot be empty")

    task_id = next_id
    next_id += 1
    tasks[task_id] = {"id": task_id, "title": task.title, "completed": False}
    return tasks[task_id]


@app.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks[task_id]["completed"] = True
    return tasks[task_id]


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    return tasks.pop(task_id)


app.mount("/static", StaticFiles(directory="app/static"), name="static")
