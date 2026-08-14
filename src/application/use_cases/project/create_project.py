from dataclasses import dataclass

from domain.ports.repositories import IProjectRepository
from domain.models.project import Project


@dataclass
class CreateProjectInput:
    id: str
    name: str
    owner_id: str
    description: str = ""


class CreateProjectUseCase:
    def __init__(self, project_repository: IProjectRepository) -> None:
        self.project_repository = project_repository

    def execute(self, input: CreateProjectInput) -> Project:
        project = Project(
            id=input.id,
            name=input.name,
            owner_id=input.owner_id,
            description=input.description,
        )
        self.project_repository.save_project(project)
        return project
