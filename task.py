from pydantic import BaseModel


class Task(BaseModel):
    name: str
    description: str
    end_date: str
    line_through: bool