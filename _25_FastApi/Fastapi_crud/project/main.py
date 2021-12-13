from fastapi import *
from sqlalchemy.sql.sqltypes import String
import database1 as db
from pydantic import BaseModel


app = FastAPI()

class Student(BaseModel):
    name : str
    age : int
    grade : str


@app.post("/add")
def add_new(student : Student):
    db.add_data(name=student.name, age=student.age, grade=student.grade)
    return {'data':'success'}

@app.delete("/del", status_code=status.HTTP_202_ACCEPTED)
def delete_record(identity):
    db.dele_data(identity)
    return {'data':'deleted'}

