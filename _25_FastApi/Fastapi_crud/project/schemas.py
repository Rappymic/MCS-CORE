from sqlalchemy.orm.session import Session
from models import Student

def add_data(name, age, grade):
    stu1 = Student(name=name, age=age, grade= grade)
    session.add(stu1)
    session.commit()

def dele_data(identity):
    stu1 = session.query(Student).filter(Student.id == identity).first()
    session.delete(stu1)
    session.commit()