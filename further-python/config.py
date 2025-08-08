PRIORITY = ["low", "medium", "high"]

DEFAULT_FILENAME = "tasks.json"

MAIN_MENU = [
    "=" * 80,
    "[1] Add a task",
    "[2] List Tasks",
    "[3] Toggle a Task's Complete Status",
    "[4] Change a Task's Priority",
    "[5] Delete a Task",
    "[6] Save Tasks",
    "[7] Load Tasks",
    "[q] Exit",
    "=" * 80,
]

ADD_MENU = [
    "[1] Add Task",
    "[q] Back",
]

DELETE_MENU = [
    "[1] Delete Task",
    "[q] Back",
]

LIST_TASKS_MENU = [
    "[1] List All Tasks",
    "[2] List Pending Tasks",
    "[3] List Complete Tasks",
    "[q] Back",
]

TOGGLE_COMPLETE_MENU = [
    "[1] Toggle a Task's Complete Status",
    "[q] Back",
]

CHANGE_PRIORITY_MENU = [
    "[1] Change a Task's Priority",
    "[q] Back",
]

SAVE_TASKS_MENU = [
    "[1] Save Tasks to File",
    "[q] Back",
]

LOAD_TASKS_MENU = [
    "[1] Load Tasks from File",
    "[q] Back",
]


CHOICE = "choice"
NAME_OF_TASK = "name of task"
TASK_ACTION = "task action"
TASK_PRIORITY = f"task priority {PRIORITY}"
NAME_OF_TASK_TO_DELETE = "name of task to delete"
NAME_OF_TASK_TO_TOGGLE = "name of task to toggle"
NAME_OF_TASK_TO_CHANGE_PRIORITY = "name of task to change Priority"
NEW_PRIORITY = "new Priority"
FILENAME = "filename"
CONFIRM_TOGGLE = "Do you wish to toggle this Task's Complete Status? (y/n) "


NAME_DISPLAY_LENGTH = 17
ACTION_DISPLAY_LENGTH = 47

PRINT_TASKS_TOP = f"{'*' * 36} Tasks {'*' * 36}"
PRINT_TASKS_BOTTOM = f"{'*' * 79}"

NO_TASKS = f"{PRINT_TASKS_TOP}\n{'[No Tasks Recorded]':^78}\n{PRINT_TASKS_BOTTOM}"
