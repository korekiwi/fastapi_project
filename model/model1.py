from model.imodel import IModel
from task import Task

_DB: list[Task] = []


class Model1(IModel):
    def save_task(self, task: Task):
        _DB.append(task)

    def dell_task(self, name_task: str):
        for i in range(len(_DB)):
            if _DB[i].name == name_task:
                _DB.pop(i)
                return

    def get_all_tasks(self) -> list[Task]:
        return _DB

    def edit_task(self, name_task: str):
        for i in range(len(_DB)):
            if _DB[i].name == name_task:
                _DB[i].line_through = True


# def foo():
#     print(999)
# if __name__ == '__main__':
#     foo()