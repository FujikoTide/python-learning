from dataclasses import dataclass


@dataclass
class CLIHandler:
    @staticmethod
    def _get_input(prompt: str) -> str:
        user_input = input(f"{prompt}: ")
        return user_input.strip().lower()
