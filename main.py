from typing import Union
from fastapi import FastAPI
from database import Base, engine, planer
from sqlalchemy import Column, Integer, String
import shemas
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)

app = FastAPI()

#test


@app.get("/")
def read_root():
    """
    Default API call
    """

    return {"Hello": "World"}

@app.post("/add")

#Definiramo funkcijo:
def create_plan(plan: shemas.planerTask):
    session =  Session(bing = engine, expire_on_commit=False)
    plandb = planer(task = plan.task)

    session.add(plandb)
    session.commit()
    id = plandb.id
    session.close()

    return f"Created new plan with id:{id}"

@app.get("/get/{id}")
def read_planer(id: int):
    return "Read plan with id {id}"

@app.put("/change/{id}")
def change_planer(id: int):
    return "Change plan with id {id}"

@app.delete("/delete/{id}")
def delete_planer(id: int):
    return "Delete plan with id {id}"

@app.get("list")
def read_plan_list():
    return "All plans"
