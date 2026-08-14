from dataclasses import dataclass

from models.task_entity import Task
from repositories import ITaskWriter, IProjectRepository


@dataclass
class CreateTaskInput:
    id: str
    task_name: str
    project_id: str
    owner_id: str


class CreateTaskUseCase:
    def __init__(
        self,
        task_repository: ITaskWriter,
        project_repository: IProjectRepository,
    ) -> None:
        self.task_repository = task_repository
        self.project_repository = project_repository

    def execute(self, input: CreateTaskInput) -> Task:
        project = self.project_repository.get_project_by_id(input.project_id)
        if not project:
            raise ValueError("El proyecto no existe")

        task = Task(
            id=input.id,
            task_name=input.task_name,
            project_id=input.project_id,
            owner_id=input.owner_id,
        )
        self.task_repository.save_task(task)
        return task
