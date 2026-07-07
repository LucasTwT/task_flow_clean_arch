from models.task_entity import Task
from repositories import ITaskRepository


class CompleteTaskUseCase:
    def __init__(self, task_repository: ITaskRepository):
        self.task_repository = task_repository

    def execute(self, task_id: str) -> Task:
        task = self.task_repository.get_task_by_id(task_id)
        if not task:
            raise ValueError("Task not found")
        task.complete()
        return task
