from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# ----------------------
# In-memory data
# ----------------------
todos = []

# ----------------------
# Model
# ----------------------
class Todo(BaseModel):
    title: str
    completed: bool = False

# ----------------------
# Create TODO
# ----------------------
@app.post("/todos")
def create_todo(todo: Todo):
    todo_data = {
        "id": len(todos) + 1,
        "title": todo.title,
        "completed": todo.completed
    }
    todos.append(todo_data)
    return todo_data

# ----------------------
# Read all TODOs
# ----------------------
@app.get("/todos")
def get_todos():
    return todos

# ----------------------
# Read single TODO
# ----------------------
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# ----------------------
# Update TODO
# ----------------------
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated: Todo):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["title"] = updated.title
            todo["completed"] = updated.completed
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# ----------------------
# Delete TODO
# ----------------------
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")
