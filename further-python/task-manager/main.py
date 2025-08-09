from task import Task
from task_manager import TaskManager
from cli_handler import CLIHandler
from task_cli import Task_CLI


def main():
    task1 = Task("test1", "cat", "low")
    task2 = Task("test2", "dog", "medium")
    task3 = Task("test3", "horse", "high")
    task4 = Task("test3", "horse", "high")
    task5 = Task("test5", "horse", "high")
    task6 = Task(
        "a very long name for testing purposes how long can this be?",
        "horsejasbnd fkjbasdkfj baskdjfbaskjdf bkjasbdfkj sjkdfbshjdfb hkb  hbhbsdfhbshjdbfjhsd shdbfhsbdf",
        "high",
    )

    task_manager = TaskManager()

    try:
        task_manager.add_task(task1)
    except ValueError as e:
        print(e)

    try:
        task_manager.add_task(task2)
    except ValueError as e:
        print(e)

    try:
        task_manager.add_task(task3)
    except ValueError as e:
        print(e)

    try:
        task_manager.add_task(task4)
    except ValueError as e:
        print(e)

    try:
        task_manager.add_task(task4)
    except ValueError as e:
        print(e)

    try:
        task_manager.add_task(task5)
    except ValueError as e:
        print(e)

    try:
        task_manager.add_task(task6)
    except ValueError as e:
        print(e)

    print(task_manager)

    task_manager.toggle_complete_task("test2")

    print(task_manager)

    cli_handler = CLIHandler()
    Task_CLI(cli_handler)


if __name__ == "__main__":
    main()
