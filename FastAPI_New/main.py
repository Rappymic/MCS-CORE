from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name : str
    number : int

@app.post('/home/post')
def post(game : Item):
    # game ------> item ---> game= {'name':'name', 'number': 12}
    new_name = game.name
    new_number = game.number
    return f'hello {new_name} you are in {new_number}'

@app.get('/home')
def get():
    return 'Hello World'

@app.get('/home/{name}')
def get(name):
    return f'Hello {name}'

@app.get('/base')
def base_fun():
    pass



# if __name__ == "__main__":
#     uvicorn.run(app, port=5000)