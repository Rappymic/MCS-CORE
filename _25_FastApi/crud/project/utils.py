from models import Employee
from sqlalchemy.orm import sessionmaker
from database import engine

Session = sessionmaker(bind=engine)

session = Session()


def add_data(name, phno, location):
    emp = Employee(name=name, phno=phno, Location=location)
    session.add(emp)
    session.commit()


def dele_data(identity):
    emp = session.query(Employee).filter(Employee.identity == identity).first()
    session.delete(emp)
    session.commit()


def update(identity, name, phone, location):
    emp = session.query(Employee).filter(Employee.identity == identity).first()
    emp.name = name
    emp.phno = phone
    emp.Location = location
    session.commit()


def get_data_all(iden):
    dic1 = {}
    emp = session.query(Employee).filter(Employee.identity == iden).first()
    dic1['identity'] = iden
    dic1['name'] = emp.name
    dic1['phone'] = emp.phno
    dic1['location'] = emp.Location
    return dic1
