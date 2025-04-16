from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class NameInput(BaseModel):
    name: str

@app.post("/hello")
async def hello(name_input: NameInput):
    return {"message": f"Hello {name_input.name}"}

@app.post("/goodbye")
async def goodbye(name_input: NameInput):
    return {"message": f"Goodbye {name_input.name}"}

