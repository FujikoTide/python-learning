from typing import List, Optional

class Task:
  def __init__(self, name: str, completed: bool = False):
    self.name= name
    self.completed = completed

  def __repr__(self):
    return f"Task: {self.name}, completed: {self.completed}"

  def complete(self):
    self.completed = True

class TaskManager:
  def __init__(self, initial_tasks: Optional[List[Task]] = None):
    self.tasks: List[Task] = initial_tasks if initial_tasks is not None else []

  def create_and_add_task(self, name: str, completed: bool = False):
    new_task = Task(name, completed)
    self.tasks.append(new_task)

  def add_existing_task(self, task: Task):
    if not isinstance(task, Task):
      raise TypeError("Only Task objects can be added")
    self.tasks.append(task)

  def get_pending_tasks(self) -> List[Task]:
    return [task for task in self.tasks if not task.completed]
  
  def get_all_tasks(self) -> List[Task]:
    return self.tasks
    