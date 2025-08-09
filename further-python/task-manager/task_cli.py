from dataclasses import dataclass
from input_handler import InputHandler
import config
from task_manager import TaskManager
from task import Task
from menu_factory import create_menu


@dataclass
class Task_CLI:
    _tasks = TaskManager()
    input_handler: InputHandler

    def __post_init__(self) -> None:
        self.run()

    def _main_menu(self) -> None:
        self._print_menu(config.MAIN_MENU)

    def _add_task(self) -> None:
        name = None
        action = None
        priority = None
        while True:
            self._print_menu(config.ADD_TASK_MENU)
            choice = self.input_handler._get_input(config.CHOICE)
            if choice == "q":
                break
            if choice == "1":
                while True:
                    if not name:
                        name = self.input_handler._get_input(config.NAME_OF_TASK)
                    if not action:
                        action = self.input_handler._get_input(config.TASK_ACTION)
                    if priority not in config.PRIORITY:
                        priority = self.input_handler._get_input(config.TASK_PRIORITY)
                    if not name or not action:
                        continue
                    if priority not in config.PRIORITY:
                        priority = None
                        continue
                    break
            if not name or not action or priority not in config.PRIORITY:
                print("Task not added.")
                continue
            task = Task(name, action, priority)
            successful_task = self._tasks.add_task(task)
            if not successful_task:
                print(f"Task {name} not added.")
                continue
            print(f"Task {name} successfully added.")

    def _delete_task(self) -> None:
        task_name = ""
        while True:
            self._print_menu(config.DELETE_TASK_MENU)
            choice = self.input_handler._get_input(config.CHOICE)
            if choice == "q":
                break
            if choice == "1":
                task_name = self.input_handler._get_input(config.NAME_OF_TASK_TO_DELETE)
            successful_task = self._tasks.remove_task(task_name)
            if not successful_task:
                print(f"Task {task_name} not found.")
                continue
            print(f"Task {task_name} successfully deleted.")

    def _list_tasks(self) -> None:
        completed = [task for task in self._tasks.tasks if task._complete]
        pending = [task for task in self._tasks.tasks if not task._complete]
        while True:
            self._print_menu(config.LIST_TASKS_MENU)
            choice = self.input_handler._get_input(config.CHOICE)
            if choice == "q":
                break
            if choice == "1":
                print(self._tasks)
            if choice == "2":
                print(self._tasks.format_tasks(pending))
            if choice == "3":
                print(self._tasks.format_tasks(completed))

    def _toggle_complete(self) -> None:
        task_name = ""
        while True:
            self._print_menu(config.TOGGLE_TASK_COMPLETE_MENU)
            choice = self.input_handler._get_input(config.CHOICE)
            if choice == "q":
                break
            if choice == "1":
                task_name = self.input_handler._get_input(config.NAME_OF_TASK_TO_TOGGLE)
                self._print_task(task_name)
                confirm_toggle = self.input_handler._get_input(config.CONFIRM_TOGGLE)
                if confirm_toggle != "y":
                    continue
                successful_task = self._tasks.toggle_complete_task(task_name)
                if not successful_task:
                    print("Operation not confirmed, Toggle has not been changed")
                    continue
                print(f"Task {task_name} set to Toggle {successful_task._complete}.")

    def _change_priority(self) -> None:
        task_name = ""
        while True:
            self._print_menu(config.CHANGE_TASK_PRIORITY_MENU)
            choice = self.input_handler._get_input(config.CHOICE)
            if choice == "q":
                break
            if choice == "1":
                task_name = self.input_handler._get_input(
                    config.NAME_OF_TASK_TO_CHANGE_PRIORITY
                )
            self._print_task(task_name)
            new_priority = self.input_handler._get_input(config.NEW_PRIORITY)
            if new_priority not in config.PRIORITY:
                print(
                    f"Priority given was not one of {config.PRIORITY}, Priority has not been changed"
                )
                continue
            successful_task = self._tasks.change_task_priority(task_name, new_priority)
            if not successful_task:
                print("Task Priority was not changed.")
                continue
            print(f"Task {task_name} Priority changed to {new_priority}")

    def _save_tasks(self) -> None:
        while True:
            self._print_menu(config.SAVE_TASKS_MENU)
            choice = self.input_handler._get_input(config.CHOICE)
            if choice == "q":
                break
            if choice == "1":
                filename = self._get_filename()
                self._tasks._storage.save_tasks(self._tasks.tasks, filename)

    def _load_tasks(self) -> None:
        while True:
            self._print_menu(config.LOAD_TASKS_MENU)
            choice = self.input_handler._get_input(config.CHOICE)
            if choice == "q":
                break
            if choice == "1":
                filename = self._get_filename()
                self._tasks._storage.load_tasks(filename)

    @staticmethod
    def _print_menu(menu: list[str]) -> None:
        for line in menu:
            print(line)

    def _print_task(self, task_name: str) -> None:
        task = self._tasks.format_tasks(
            [task for task in self._tasks.tasks if task.name == task_name]
        )
        print(task)

    def _get_filename(self) -> str:
        filename = self.input_handler._get_input(config.FILENAME)
        if filename == "":
            filename = config.DEFAULT_FILENAME
        return filename

    def run(self) -> None:
        menu = create_menu(self)
        while True:
            self._main_menu()
            choice = self.input_handler._get_input(config.CHOICE)
            if choice == "q":
                break
            menu[choice]()
