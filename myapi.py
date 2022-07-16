# python -m pip install fastapi
# pip install uvicorn
# python - m uvicorn main: app - -reload
# GET - GET AN Response
# POST CREATE SOMETHING NEW
# PUT - UPDATE
# DELETE - DELETE SOMETHING

from lib2to3.pgen2.token import OP
from this import s
from tokenize import Name
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# def dictionary with some data
students = {
    1: {
        "name": "Riz",
        "age": 17,
        "class": 12
    },
    2: {
        "name": "Deb",
        "age": 17,
        "class": 12
    }
}

# def Student model to create new entry


class Student(BaseModel):
    name: str
    age: int
    year: str

# def UpdateStudent model to update exiting entry


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

# test


@app.get("/")
def index():
    return {"name": "First Data"}

# display student data by id


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student you want to view", gt=0, lt=15)):
    return students[student_id]

# display student data by name & id


@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}

# create new entry


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student
    return students[student_id]

# update existing entry


@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

# delete existing entry


@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return{"Error": "Student does not exist"}
    del students[student_id]
    return {"Message": "Student deleted successful"}
