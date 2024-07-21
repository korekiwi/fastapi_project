from model.model1 import Model1
from vies.ConsoleVies import ConsoleVies
from controler.consol_controler import ConsoleControler
from vies.new_vies import NewVies


def main():
    model = Model1()
    vies = ConsoleVies()
    contr = ConsoleControler(
        model=model, vies=vies
    )
    while True:
        user_input = input("1 - add task\n"
                           "2 - get all tasks\n"
                           "3 - dell task")
        if user_input == "1":
            contr.save_task()
        if user_input == "2":
            contr.get_all_tasks()
        if user_input == "3":
            contr.dell_task()
        if user_input == "0":
            exit(0)


if __name__ == '__main__':
    main()
