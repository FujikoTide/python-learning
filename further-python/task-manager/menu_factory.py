# GET_INPUT = {"1": "input_handler._get_input"}

# LIST_TASKS = {
#     "1": "_tasks",
#     "2": "_tasks.format_tasks",
# }

from collections.abc import Callable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from task_cli import Task_CLI


def create_menu(manager: Task_CLI) -> dict[str, Callable[[], None]]:
    return {
        "1": manager._add_task,
        "2": manager._list_tasks,
        "3": manager._toggle_complete,
        "4": manager._change_priority,
        "5": manager._delete_task,
        "6": manager._save_tasks,
        "7": manager._load_tasks,
    }
