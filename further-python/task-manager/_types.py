from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from task import Task

Tasks = list["Task"]


class TaskData(TypedDict):
    name: str
    action: str
    priority: str
    complete: bool
