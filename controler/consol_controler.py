from task import Task
from model.imodel import IModel
from vies.IVies import IVies


class ConsoleControler:
    def __init__(self, model: IModel, vies: IVies):
        self.model = model
        self.vies = vies

    def save_task(self):
        task = self.vies.get_task()
        self.model.save_task(task)

    def dell_task(self):
        name_task = self.vies.dell_task()
        self.model.dell_task(name_task)

    def get_all_tasks(self):
        tasks = self.model.get_all_tasks()
        self.vies.print_all_task(tasks)

    def edit_task(self):
        name_task = self.vies.edit_task()
        self.model.edit_task(name_task)



class FastapiControler:
    def __init__(self, model: IModel):
        self.model = model

    def save_task(self, task: Task):
        self.model.save_task(task)

    def dell_task(self, name_task: str):
        self.model.dell_task(name_task)

    def get_all_tasks(self) -> list[Task]:
        return self.model.get_all_tasks()

    def edit_task(self, name_task: str):
        self.model.edit_task()