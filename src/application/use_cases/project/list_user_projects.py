from models.project import Project
from repositories import IProjectRepository


class ListUserProjectsUseCase:
    def __init__(self, project_repository: IProjectRepository):
        self.project_repository = project_repository

    def execute(self, user_id: str) -> list[Project]:
        return self.project_repository.get_projects(user_id)
