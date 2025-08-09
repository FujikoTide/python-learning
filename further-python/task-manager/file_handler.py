from dataclasses import dataclass
from typing import Protocol
from _types import Tasks


@dataclass
class FileHandler(Protocol):
    @classmethod
    def save_tasks(cls, tasks: Tasks, filename: str) -> None: ...

    @classmethod
    def load_tasks(cls, filename: str) -> Tasks: ...
