from pydantic import BaseModel

class Article_check(BaseModel):
    title : str
    body : str

class User_details(BaseModel):
    user_name : str
    password : str