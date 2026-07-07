from models.task_entity import Task
from repositories import ITaskRepository, IProjectRepository


class ListProjectTasksUseCase:
    def __init__(
        self,
        task_repository: ITaskRepository,
        project_repository: IProjectRepository,
    ) -> None:
        self.task_repository = task_repository
        self.project_repository = project_repository

    def execute(self, project_id: str) -> list[Task]:
        project = self.project_repository.get_project_by_id(project_id)
        if not project:
            raise ValueError("El proyecto no existe")

        return self.task_repository.get_task_by_project_id(project_id)
