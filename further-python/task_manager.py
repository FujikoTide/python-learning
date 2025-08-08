# add custom errors
# refactor


from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import json
import textwrap
import os
from typing import TypedDict
import config


class TaskData(TypedDict):
    name: str
    action: str
    priority: str
    complete: bool


class InvalidPriority(ValueError):
    def __init__(self) -> None:
        super().__init__(f"Priority must be one of: {config.PRIORITY}")


class TaskNotFound(ValueError):
    def __init__(self, task_name: str) -> None:
        super().__init__(f"Task does not exist: {task_name}")


class NameError(ValueError):
    def __init__(self) -> None:
        super().__init__("Task names must be unique.")


@dataclass
class Task:
    name: str
    action: str
    priority: str = "low"
    _complete: bool = field(init=False)

    def __post_init__(self) -> None:
        if self.priority not in config.PRIORITY:
            raise InvalidPriority()
        self._complete = False

    def to_dict(self) -> dict[str, str | bool]:
        return {
            "name": self.name,
            "action": self.action,
            "priority": self.priority,
            "complete": self._complete,
        }

    @classmethod
    def from_dict(cls, data: TaskData) -> "Task":
        task = cls(data["name"], data["action"], data["priority"])
        if data["complete"]:
            task.toggle_complete()
        return task

    def change_priority(self, priority: str) -> None:
        if priority in config.PRIORITY:
            self.priority = priority
        else:
            raise InvalidPriority()

    def toggle_complete(self) -> None:
        self._complete = not self._complete


@dataclass
class FileHandler(ABC):
    @classmethod
    @abstractmethod
    def save_tasks(cls, tasks: list[Task], filename: str) -> None:
        pass

    @classmethod
    @abstractmethod
    def load_tasks(cls, filename: str) -> list[Task]:
        pass


@dataclass
class JSONStorage(FileHandler):
    @classmethod
    def save_tasks(
        cls, tasks: list[Task], filename: str = config.DEFAULT_FILENAME
    ) -> None:
        tasks_dict = [task.to_dict() for task in tasks]
        print(tasks_dict)
        with open(filename, "w") as f:
            f.write(json.dumps(tasks_dict))

    @classmethod
    def load_tasks(cls, filename: str = config.DEFAULT_FILENAME) -> list[Task]:
        with open(filename) as f:
            tasks = json.load(f)
            print(tasks)
            list_of_tasks = [Task.from_dict(task) for task in tasks]
            print(list_of_tasks)
            return list_of_tasks


@dataclass
class TaskManager:
    tasks: list[Task] = field(default_factory=list[Task])
    _name_display_length: int = config.NAME_DISPLAY_LENGTH
    _action_display_length: int = config.ACTION_DISPLAY_LENGTH
    _storage: FileHandler = field(default_factory=JSONStorage)

    def __post_init__(self) -> None:
        if not self.tasks and os.path.exists(config.DEFAULT_FILENAME):
            self.tasks = self._storage.load_tasks(config.DEFAULT_FILENAME)

    def __str__(self) -> str:
        return self.format_tasks(self.tasks)

    def add_task(self, task: Task) -> None:
        task_exists = self._get_task_by_name(task.name)
        if not task_exists:
            self.tasks.append(task)
        else:
            raise NameError()

    def remove_task(self, task_name: str) -> None:
        task_to_remove = self._get_task_by_name(task_name)
        if task_to_remove:
            self.tasks.remove(task_to_remove)
        else:
            raise TaskNotFound(task_name)

    def toggle_complete_task(self, task_name: str) -> None:
        task_to_toggle = self._get_task_by_name(task_name)
        if task_to_toggle:
            task_to_toggle.toggle_complete()
        else:
            raise TaskNotFound(task_name)

    def change_task_priority(self, task_name, new_priority: str) -> None:
        task_to_toggle = self._get_task_by_name(task_name)
        if task_to_toggle:
            task_to_toggle.change_priority(new_priority)
        else:
            raise TaskNotFound(task_name)

    def _get_task_by_name(self, task_name: str) -> Task | None:
        return next((task for task in self.tasks if task.name == task_name), None)

    def format_tasks(self, tasks: list[Task]) -> str:
        if tasks:
            print_tasks = []
            name_max_length = max([len(task.name) for task in tasks]) + len("[]")
            if name_max_length > self._name_display_length:
                name_max_length = self._name_display_length

            action_max_length = max([len(task.action) for task in tasks]) + len("[]")
            if action_max_length > self._action_display_length:
                action_max_length = self._action_display_length

            priority_max_length = max([len(task.priority) for task in tasks]) + len(
                "[]"
            )

            for task in tasks:
                name = task.name
                if len(task.name) > self._name_display_length:
                    name = textwrap.shorten(
                        task.name, self._name_display_length, placeholder="..."
                    )
                name = f"[{name}]"

                action = task.action
                if len(task.action) > self._action_display_length:
                    action = textwrap.shorten(
                        task.action, self._action_display_length, placeholder="..."
                    )
                action = f"[{action}]"

                priority = f"[{task.priority}]"
                complete = "[Complete]" if task._complete else "[Incomplete]"

                task_output = f"{name:{name_max_length}} {action:{action_max_length}} {priority:{priority_max_length}} {complete}"

                print_tasks.append(task_output)

            formatted_tasks = "\n".join(print_tasks)
            return f"{config.PRINT_TASKS_TOP}\n{formatted_tasks}\n{config.PRINT_TASKS_BOTTOM}"
        return config.NO_TASKS


@dataclass
class Task_CLI:
    _tasks = TaskManager()

    def __post_init__(self) -> None:
        self.run()

    @classmethod
    def _get_user_input(cls, prompt: str) -> str:
        user_input = input(prompt)
        return user_input.strip().lower()

    @classmethod
    def _main_menu(cls) -> None:
        cls._print_menu(config.MAIN_MENU)

    @classmethod
    def _add_task(cls) -> Task:
        name = None
        action = None
        priority = None
        while True:
            if name is None:
                name = cls._get_input(config.NAME_OF_TASK)
            if action is None:
                action = cls._get_input(config.TASK_ACTION)
            if priority is None:
                priority = cls._get_input(config.TASK_PRIORITY)
            if priority not in config.PRIORITY:
                priority = None
                continue
            return Task(name, action, priority)

    @classmethod
    def _delete_task(cls) -> None:
        task_name = ""
        while True:
            cls._print_menu(config.DELETE_MENU)
            choice = cls._get_input(config.CHOICE)
            if choice == "q":
                break
            if choice == "1":
                task_name = cls._get_input(config.NAME_OF_TASK_TO_DELETE)
            try:
                task_exists = cls._tasks._get_task_by_name(task_name)
                if task_exists:
                    cls._tasks.remove_task(task_name)
            except TaskNotFound as e:
                print(e)
            else:
                print(f"Task {task_name} successfully deleted.")

    @classmethod
    def _list_tasks(cls) -> None:
        completed = [task for task in cls._tasks.tasks if task._complete]
        pending = [task for task in cls._tasks.tasks if not task._complete]
        while True:
            cls._print_menu(config.LIST_TASKS_MENU)
            choice = cls._get_input(config.CHOICE)
            if choice == "q":
                break
            if choice == "1":
                print(cls._tasks)
            if choice == "2":
                print(cls._tasks.format_tasks(pending))
            if choice == "3":
                print(cls._tasks.format_tasks(completed))

    @classmethod
    def _toggle_complete(cls) -> None:
        task_name = ""
        completed = False
        while True:
            cls._print_menu(config.TOGGLE_COMPLETE_MENU)
            choice = cls._get_input(config.CHOICE)
            if choice == "q":
                break
            if choice == "1":
                task_name = cls._get_input(config.NAME_OF_TASK_TO_TOGGLE)
            try:
                task_exists = cls._tasks._get_task_by_name(task_name)
                if task_exists:
                    completed = task_exists._complete
                    cls._print_task(task_name)
                    confirm_toggle = cls._get_input(config.CONFIRM_TOGGLE)
                    if confirm_toggle == "y":
                        cls._tasks.toggle_complete_task(task_name)
                    else:
                        print("Operation not confirmed, Toggle has not been changed")
                        continue
                    cls._print_task(task_name)
                    continue
            except TaskNotFound as e:
                print(e)
            else:
                print(
                    f"Task {task_name} set to {'Complete' if completed else 'Incomplete'}."
                )

    @classmethod
    def _change_priority(cls) -> None:
        task_name = ""
        new_priority = ""
        while True:
            cls._print_menu(config.CHANGE_PRIORITY_MENU)
            choice = cls._get_input(config.CHOICE)
            if choice == "q":
                break
            if choice == "1":
                task_name = cls._get_input(config.NAME_OF_TASK_TO_CHANGE_PRIORITY)
            try:
                task_exists = cls._tasks._get_task_by_name(task_name)
                if task_exists:
                    cls._print_task(task_name)
                    new_priority = cls._get_input(config.NEW_PRIORITY)
                    if new_priority in config.PRIORITY:
                        cls._tasks.change_task_priority(task_name, new_priority)
                    else:
                        print(
                            f"Priority given was not one of {config.PRIORITY}, Priority has not been changed"
                        )
                        continue
                    cls._print_task(task_name)
                    continue
            except TaskNotFound as e:
                print(e)
            else:
                print(f"Task {task_name} Priority changed to: {new_priority}")

    @classmethod
    def _save_tasks(cls) -> None:
        while True:
            cls._print_menu(config.SAVE_TASKS_MENU)
            choice = cls._get_input(config.CHOICE)
            if choice == "q":
                break
            if choice == "1":
                filename = cls._get_filename()
                cls._tasks._storage.save_tasks(cls._tasks.tasks, filename)

    @classmethod
    def _load_tasks(cls) -> None:
        while True:
            cls._print_menu(config.LOAD_TASKS_MENU)
            choice = cls._get_input(config.CHOICE)
            if choice == "q":
                break
            if choice == "1":
                filename = cls._get_filename()
                cls._tasks._storage.load_tasks(filename)

    @staticmethod
    def _print_menu(menu: list[str]) -> None:
        for line in menu:
            print(line)

    @staticmethod
    def _print_task(task_name) -> None:
        task = Task_CLI._tasks.format_tasks(
            [task for task in Task_CLI._tasks.tasks if task.name == task_name]
        )
        print(task)

    @staticmethod
    def _get_input(prompt: str, prefix: bool = True) -> str:
        pe = "Please enter "
        if not prefix:
            pe = ""
        return Task_CLI._get_user_input(f"{pe}{prompt}: ")

    @staticmethod
    def _get_filename() -> str:
        filename = Task_CLI._get_input(config.FILENAME)
        if filename == "":
            filename = config.DEFAULT_FILENAME
        return filename

    @staticmethod
    def run() -> None:
        while True:
            Task_CLI._main_menu()
            choice = Task_CLI._get_input(config.CHOICE)
            if choice == "q":
                break
            if choice == "1":
                task = Task_CLI._add_task()
                try:
                    Task_CLI._tasks.add_task(task)
                except NameError as e:
                    print(e)
            if choice == "2":
                Task_CLI._list_tasks()
            if choice == "3":
                Task_CLI._toggle_complete()
            if choice == "4":
                Task_CLI._change_priority()
            if choice == "5":
                Task_CLI._delete_task()
            if choice == "6":
                Task_CLI._save_tasks()
            if choice == "7":
                Task_CLI._load_tasks()


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

Task_CLI()
