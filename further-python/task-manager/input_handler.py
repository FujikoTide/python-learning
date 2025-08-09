from dataclasses import dataclass
from typing import Protocol


@dataclass
class InputHandler(Protocol):
    @staticmethod
    def _get_input(prompt: str) -> str: ...
