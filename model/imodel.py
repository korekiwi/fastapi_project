from task import Task
from abc import ABC, abstractmethod


class IModel(ABC):
    @abstractmethod
    def save_task(self, task: Task):
        pass

    @abstractmethod
    def dell_task(self, name_task: str):
        pass

    @abstractmethod
    def get_all_tasks(self) -> list[Task]:
        pass

    @abstractmethod
    def edit_task(self, name_task: str):
        pass
