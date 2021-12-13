from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'
    identity = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    phno = Column(Integer)
    Location = Column(String(50))

