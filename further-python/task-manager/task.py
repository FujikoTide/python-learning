from dataclasses import dataclass, field
import config
import exceptions
from _types import TaskData


@dataclass
class Task:
    name: str
    action: str
    priority: str = "low"
    _complete: bool = field(init=False)

    def __post_init__(self) -> None:
        if self.priority not in config.PRIORITY:
            raise exceptions.InvalidPriority()
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
            raise exceptions.InvalidPriority()

    def toggle_complete(self) -> None:
        self._complete = not self._complete
