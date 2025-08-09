from __future__ import annotations
from dataclasses import dataclass, field
import textwrap
import os
import config
from task import Task
from file_handler import FileHandler
from json_storage import JSONStorage
from _types import Tasks


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

    def add_task(self, task: Task) -> Task | None:
        task_exists = self._get_task_by_name(task.name)
        if task_exists:
            return task_exists
        self.tasks.append(task)
        return None

    def remove_task(self, task_name: str) -> Task | None:
        task_to_remove = self._get_task_by_name(task_name)
        if not task_to_remove:
            return None
        self.tasks.remove(task_to_remove)
        return task_to_remove

    def toggle_complete_task(self, task_name: str) -> Task | None:
        task_to_toggle = self._get_task_by_name(task_name)
        if not task_to_toggle:
            return None
        task_to_toggle.toggle_complete()
        return task_to_toggle

    def change_task_priority(self, task_name: str, new_priority: str) -> Task | None:
        task_to_change_priority = self._get_task_by_name(task_name)
        if not task_to_change_priority:
            return None
        task_to_change_priority.change_priority(new_priority)
        return task_to_change_priority

    def _get_task_by_name(self, task_name: str) -> Task | None:
        return next((task for task in self.tasks if task.name == task_name), None)

    def format_tasks(self, tasks: Tasks) -> str:
        if not tasks:
            return config.NO_TASKS

        print_tasks = []
        name_max_length = self._clamp_to_max_length("name")
        action_max_length = self._clamp_to_max_length("action")
        priority_max_length = self._get_max_length("priority")

        for task in tasks:
            name = self._format_property(task, "name")
            action = self._format_property(task, "action")
            priority = f"[{task.priority}]"
            complete = "[Complete]" if task._complete else "[Incomplete]"
            task_output = f"{name:{name_max_length}} {action:{action_max_length}} {priority:{priority_max_length}} {complete}"
            print_tasks.append(task_output)

        formatted_tasks = "\n".join(print_tasks)
        return (
            f"{config.PRINT_TASKS_TOP}\n{formatted_tasks}\n{config.PRINT_TASKS_BOTTOM}"
        )

    def _get_max_length(self, name_of_property: str) -> int:
        return max([len(getattr(task, name_of_property)) for task in self.tasks]) + len(
            "[]"
        )

    def _clamp_to_max_length(self, property_identifier_fragment: str) -> int:
        max_length = self._get_max_length(property_identifier_fragment)
        property_display_length = self._get_display_length(property_identifier_fragment)

        if max_length < property_display_length:
            return max_length
        return property_display_length

    def _format_property(self, task: Task, name_of_property: str) -> str:
        name = getattr(task, name_of_property)
        property_display_length = self._get_display_length(name_of_property)

        if len(name) < property_display_length:
            return f"[{name}]"

        truncated_name = textwrap.shorten(
            name, property_display_length, placeholder="..."
        )
        return f"[{truncated_name}]"

    def _get_display_length(self, property_identifier_fragment: str) -> int:
        property_name = f"_{property_identifier_fragment}_display_length"
        return getattr(self, property_name)
