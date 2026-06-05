from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    task: str

@app.get("/")
def root():
    return {"status": "AgentOS Running"}

@app.post("/task")
def run_task(data: Task):
    return {"result": f"received: {data.task}"}
