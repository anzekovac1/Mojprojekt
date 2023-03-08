from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///planerdatabase.db")

Base = declarative_base()

class planer(Base):  # prej ToDo
    __tablename__="testplan"
    id = Column(Integer, primary_key=True)
    task = Column(String(50))