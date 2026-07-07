from models.task_entity import Task
from repositories import ITaskRepository


class ReopenTaskUseCase:
    def __init__(self, task_repository: ITaskRepository) -> None:
        self.task_repository = task_repository

    def execute(self, task_id: str) -> Task:
        task = self.task_repository.get_task_by_id(task_id)
        if not task:
            raise ValueError("La tarea no existe")
        if not task.get_status():
            raise ValueError("La tarea no está completada — no se puede reabrir")
        task.reopen()
        return task
