from cgitb import text
from sqlalchemy import create_engine, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///new1.db', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Article(Base):
    __tablename__ = 'Article'
    identity = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    body = Column(Text)

class User_data(Base):
    __tablename__ = 'User_Data'
    identity = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(16))
    password = Column(Text)


Base.metadata.create_all(engine)

