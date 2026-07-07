from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
'''#endpoint1 cu path para(/hello/ana)
@app.get("/hello/{name}")
def home(name:str):
    return {"message": f"Hello {name}"}

#endpoint2 cu  query para(/sum?a=2&b=3)
@app.get("/sum")
def sum(a: int, b: int):
    return {
        "result": a + b
    }
'''
#endpoint3 cu request body(testat cu swagger UI & Postman)
class Student(BaseModel):
    name: str
    age: int
    faculty: str

@app.post("/students")
def create_student(student:Student):
    return {
        "message":"student created",
        "student_name": student.name,
        "student_age": student.age,
        "student_faculty": student.faculty
    }