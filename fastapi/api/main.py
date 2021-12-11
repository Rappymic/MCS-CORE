from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import database11 as db
import uvicorn

app = FastAPI()

class Data(BaseModel):
    title : str
    body : str
    id : Optional[int] = None

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/test/{no}")
def test(no: int):
    return {"data":f"{no}"}

@app.post('/add_blog')
def add_blog(data : Data):
    db.create_blog(data.title, data.body)
    return {'data': 'created'}
 