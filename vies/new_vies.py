from vies.IVies import IVies

from task import Task


class NewVies(IVies):
    def get_task(self,
                 mes_name: str = "Введите имя задачи\n",
                 mes_description: str = "description",
                 mes_end_date: str = "end_date") -> Task:
        name = input(mes_name)
        description = input(mes_description)
        end_date = input(mes_end_date)
        print("NEW VIES")
        return Task(
            name=name,
            description=description,
            end_date=end_date
        )

    def dell_task(self, mes: str = "введите имя задачи для удаления") -> str:
        print("NEW VIES")
        return input(mes)

    def print_all_task(self, tasks: list[Task]):
        print("NEW VIES")
        for task in tasks:
            print(task)
            print("*" * 50)
