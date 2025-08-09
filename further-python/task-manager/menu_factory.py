# MAIN_MENU = {
#     "1": "_add_task",
#     "2": "_list_tasks",
#     "3": "_toggle_complete",
#     "4": "_change_priority",
#     "5": "_delete_task",
#     "6": "_save_tasks",
#     "7": "_load_tasks",
# }

# GET_INPUT = {"1": "input_handler._get_input"}

# LIST_TASKS = {
#     "1": "_tasks",
#     "2": "_tasks.format_tasks",
# }


def create_menu(manager):
    return {
        "1": manager._add_task,
        "2": manager._list_tasks,
        "3": manager._toggle_complete,
        "4": manager._change_priority,
        "5": manager._delete_task,
        "6": manager._save_tasks,
        "7": manager._load_tasks,
    }
