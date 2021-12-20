from fastapi import *
import schemas as s
import utils as u

app = FastAPI()


@app.post('/home')
def home(data: s.Emp_add):
    u.add_data(name=data.name, location=data.location, phno=data.phno)
    return {'data': 'done'}


@app.delete('/del', status_code=status.HTTP_202_ACCEPTED)
def delete_data(data: s.Emp_del):
    u.dele_data(identity=data.identity)
    return {'data': 'done'}


@app.put('/update', status_code=status.HTTP_202_ACCEPTED)
def update(data: s.Emp_add):
    u.update(identity=data.iden, name=data.name, location=data.location,
             phone=data.phno)
    return {'data': 'completed'}


@app.get('/hom/{i}')
def get_data(i: int):
    return u.get_data_all(i)
