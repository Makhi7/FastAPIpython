from typing import Optional
from fastapi import FastAPI,Path

# create API obj
# to access it later with getter and setters
app = FastAPI()

# dictionary
students = {
    1:{
        "name":"john",
        "age": 17,
        "grade":"year 12"
    }
}

# create an end point for communication channel url
# e.g localhost/delete-user
# types of ende user point
# GET - get info
# Post - create something new
# Put - Update
# Delete - Delete something
@app.get("/")
def index():
    return{"name":"First Data"}

# endpoint parameter 
# returns data relating to input
@app.get("/get-student/{student_id}")
def index(student_id: int =Path(None, description = "The ID of student I want to view", gt=0, lt=3)):
    return students[student_id]


# query parameters
# is used to pass a value to a url
@app.get("/get-by-name")
def get_student(name : Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return{"Data":"Not found"}

# combining path and query parameters