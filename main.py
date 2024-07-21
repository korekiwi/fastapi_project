# import json
# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     def __str__(self):
#         return str(self.__dict__)
#
#     @abstractmethod
#     def save(self, file_path: str):
#         pass
#
#     @classmethod
#     def load(cls, file_path: str):
#         with open(file_path, 'r', encoding="utf-8") as f:
#             data = json.load(f)
#         return cls(**data)
#
#
# class Square(Shape):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def save(self, file_path: str):
#         with open(file_path, 'w', encoding="utf-8") as f:
#             json.dump(obj=self.__dict__,
#                       fp=f)
#
#
# class Square999(Shape):
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def save(self, file_path: str):
#         with open(file_path, 'w', encoding="utf-8") as f:
#             json.dump(obj=self.__dict__,
#                       fp=f)
#

# x = Square(9, 100)
# x.save("sq.json")
# print(x)
# new_x = Square.load("sq.json")
# print(new_x)
# square999 = Square999(1, 2, 3)
# square999.save("sq1.json")
# new_square999 = Square999.load("sq1.json")
# print(square999)
# print(new_square999)

# def foo(x, *args, **kwargs):
#     print(x)
#     print(args)
#     print(kwargs)
#
#
# foo("foo")

from typing import Union
from fastapi import FastAPI
from controler.consol_controler import FastapiControler
from model.model1 import Model1
from task import Task
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=False, allow_methods=["*"], allow_headers=["*"])

model = Model1()
contr = FastapiControler(model=model)
# CRUD


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/create_task/")
def read_item(name: str, description: str, end_date: str, line_through: bool):
    model.save_task(Task(
        name=name,
        description=description,
        end_date=end_date,
        line_through=line_through
    ))
    return {"message": "ok"}


@app.get("/dell_task/")
def dell_task(name: str):
    model.dell_task(name)
    return {"message": "ok"}


@app.get("/get_all_tasks/")
def get_all_tasks() -> list[Task]:
    return model.get_all_tasks()

@app.get("/edit_task/")
def edit_task(name: str):
    model.edit_task(name)
    return {"message": "ok"}