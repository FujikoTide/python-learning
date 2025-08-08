# add custom errors
# refactor


from __future__ import annotations
from dataclasses import dataclass, field
import json
import textwrap
import os
from typing import Protocol, TypedDict
import config


class TaskData(TypedDict):
    name: str
    action: str
    priority: str
    complete: bool


Tasks = list["Task"]


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

    def to_dict(self) -> TaskData:
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
class FileHandler(Protocol):
    @classmethod
    def save_tasks(cls, tasks: Tasks, filename: str) -> None: ...

    @classmethod
    def load_tasks(cls, filename: str) -> Tasks: ...


@dataclass
class JSONStorage:
    @classmethod
    def save_tasks(cls, tasks: Tasks, filename: str = config.DEFAULT_FILENAME) -> None:
        tasks_dict = [task.to_dict() for task in tasks]
        print(tasks_dict)
        with open(filename, "w") as f:
            f.write(json.dumps(tasks_dict))

    @classmethod
    def load_tasks(cls, filename: str = config.DEFAULT_FILENAME) -> Tasks:
        with open(filename) as f:
            tasks = json.load(f)
            print(tasks)
            list_of_tasks = [Task.from_dict(task) for task in tasks]
            print(list_of_tasks)
            return list_of_tasks


@dataclass
class TaskManager:
    tasks: Tasks = field(default_factory=Tasks)
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

    def change_task_priority(self, task_name: str, new_priority: str) -> None:
        task_to_toggle = self._get_task_by_name(task_name)
        if task_to_toggle:
            task_to_toggle.change_priority(new_priority)
        else:
            raise TaskNotFound(task_name)

    def _get_task_by_name(self, task_name: str) -> Task | None:
        return next((task for task in self.tasks if task.name == task_name), None)

    def format_tasks(self, tasks: Tasks) -> str:
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
class InputHandler(Protocol):
    @staticmethod
    def _get_input(prompt: str, prefix: str = "") -> str: ...


@dataclass
class CLIHandler:
    @staticmethod
    def _get_input(prompt: str, prefix: str = "") -> str:
        user_input = input(f"{prefix}{prompt}: ")
        return user_input.strip().lower()


@dataclass
class Task_CLI:
    _tasks = TaskManager()
    input_handler: InputHandler

    def __post_init__(self) -> None:
        self.run()

    def _main_menu(self) -> None:
        self._print_menu(config.MAIN_MENU)

    def _add_task(self) -> Task:
        name = None
        action = None
        priority = None
        while True:
            if name is None:
                name = self.input_handler._get_input(
                    config.NAME_OF_TASK, config.PLEASE_ENTER
                )
            if action is None:
                action = self.input_handler._get_input(
                    config.TASK_ACTION, config.PLEASE_ENTER
                )
            if priority is None:
                priority = self.input_handler._get_input(
                    config.TASK_PRIORITY, config.PLEASE_ENTER
                )
            if priority not in config.PRIORITY:
                priority = None
                continue
            return Task(name, action, priority)

    def _delete_task(self) -> None:
        task_name = ""
        while True:
            self._print_menu(config.DELETE_MENU)
            choice = self.input_handler._get_input(config.CHOICE, config.PLEASE_ENTER)
            if choice == "q":
                break
            if choice == "1":
                task_name = self.input_handler._get_input(
                    config.NAME_OF_TASK_TO_DELETE, config.PLEASE_ENTER
                )
            try:
                task_exists = self._tasks._get_task_by_name(task_name)
                if task_exists:
                    self._tasks.remove_task(task_name)
            except TaskNotFound as e:
                print(e)
            else:
                print(f"Task {task_name} successfully deleted.")

    def _list_tasks(self) -> None:
        completed = [task for task in self._tasks.tasks if task._complete]
        pending = [task for task in self._tasks.tasks if not task._complete]
        while True:
            self._print_menu(config.LIST_TASKS_MENU)
            choice = self.input_handler._get_input(config.CHOICE, config.PLEASE_ENTER)
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
        completed = False
        while True:
            self._print_menu(config.TOGGLE_COMPLETE_MENU)
            choice = self.input_handler._get_input(config.CHOICE, config.PLEASE_ENTER)
            if choice == "q":
                break
            if choice == "1":
                task_name = self.input_handler._get_input(
                    config.NAME_OF_TASK_TO_TOGGLE, config.PLEASE_ENTER
                )
            try:
                task_exists = self._tasks._get_task_by_name(task_name)
                if task_exists:
                    completed = task_exists._complete
                    self._print_task(task_name)
                    confirm_toggle = self.input_handler._get_input(
                        config.CONFIRM_TOGGLE
                    )
                    if confirm_toggle == "y":
                        self._tasks.toggle_complete_task(task_name)
                    else:
                        print("Operation not confirmed, Toggle has not been changed")
                        continue
                    self._print_task(task_name)
                    continue
            except TaskNotFound as e:
                print(e)
            else:
                print(
                    f"Task {task_name} set to {'Complete' if completed else 'Incomplete'}."
                )

    def _change_priority(self) -> None:
        task_name = ""
        new_priority = ""
        while True:
            self._print_menu(config.CHANGE_PRIORITY_MENU)
            choice = self.input_handler._get_input(config.CHOICE, config.PLEASE_ENTER)
            if choice == "q":
                break
            if choice == "1":
                task_name = self.input_handler._get_input(
                    config.NAME_OF_TASK_TO_CHANGE_PRIORITY, config.PLEASE_ENTER
                )
            try:
                task_exists = self._tasks._get_task_by_name(task_name)
                if task_exists:
                    self._print_task(task_name)
                    new_priority = self.input_handler._get_input(
                        config.NEW_PRIORITY, config.PLEASE_ENTER
                    )
                    if new_priority in config.PRIORITY:
                        self._tasks.change_task_priority(task_name, new_priority)
                    else:
                        print(
                            f"Priority given was not one of {config.PRIORITY}, Priority has not been changed"
                        )
                        continue
                    self._print_task(task_name)
                    continue
            except TaskNotFound as e:
                print(e)
            else:
                print(f"Task {task_name} Priority changed to: {new_priority}")

    def _save_tasks(self) -> None:
        while True:
            self._print_menu(config.SAVE_TASKS_MENU)
            choice = self.input_handler._get_input(config.CHOICE, config.PLEASE_ENTER)
            if choice == "q":
                break
            if choice == "1":
                filename = self._get_filename()
                self._tasks._storage.save_tasks(self._tasks.tasks, filename)

    def _load_tasks(self) -> None:
        while True:
            self._print_menu(config.LOAD_TASKS_MENU)
            choice = self.input_handler._get_input(config.CHOICE, config.PLEASE_ENTER)
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
        filename = self.input_handler._get_input(config.FILENAME, config.PLEASE_ENTER)
        if filename == "":
            filename = config.DEFAULT_FILENAME
        return filename

    def run(self) -> None:
        while True:
            self._main_menu()
            choice = self.input_handler._get_input(config.CHOICE, config.PLEASE_ENTER)
            if choice == "q":
                break
            if choice == "1":
                task = self._add_task()
                self._tasks.add_task(task)
            if choice == "2":
                self._list_tasks()
            if choice == "3":
                self._toggle_complete()
            if choice == "4":
                self._change_priority()
            if choice == "5":
                self._delete_task()
            if choice == "6":
                self._save_tasks()
            if choice == "7":
                self._load_tasks()


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
