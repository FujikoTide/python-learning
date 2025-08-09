from dataclasses import dataclass
import json
from config import DEFAULT_FILENAME
from task import Task
from _types import Tasks


@dataclass
class JSONStorage:
    @classmethod
    def save_tasks(cls, tasks: Tasks, filename: str = DEFAULT_FILENAME) -> None:
        tasks_dict = [task.to_dict() for task in tasks]
        print(tasks_dict)
        with open(filename, "w") as f:
            f.write(json.dumps(tasks_dict))

    @classmethod
    def load_tasks(cls, filename: str = DEFAULT_FILENAME) -> Tasks:
        with open(filename) as f:
            tasks = json.load(f)
            print(tasks)
            list_of_tasks = [Task.from_dict(task) for task in tasks]
            print(list_of_tasks)
            return list_of_tasks
