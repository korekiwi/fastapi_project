from abc import ABC, abstractmethod

from task import Task


class IVies(ABC):
    @abstractmethod
    def get_task(self) -> Task:
        """Будет запрашивать данные для заадчи"""
        pass

    @abstractmethod
    def print_all_task(self, tasks: list[Task]):
        pass

    @abstractmethod
    def dell_task(self) -> str:
        pass

    @abstractmethod
    def edit_task(self):
        pass
