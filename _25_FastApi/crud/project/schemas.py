from pydantic import BaseModel
from typing import Optional

class Emp_add(BaseModel):
    name : str
    phno : int
    location : str
    iden : Optional[int]

class Emp_del(BaseModel):
    identity : int