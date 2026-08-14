from domain.models.task import Task
from domain.ports.repositories import ITaskReader


class GetUserTasksUseCase:
    def __init__(self, task_repository: ITaskReader) -> None:
        self.task_repository = task_repository

    def execute(self, user_id: str) -> list[Task]:
        return self.task_repository.get_tasks_by_assigned_user(user_id)
