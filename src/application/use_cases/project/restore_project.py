from models.project import Project
from repositories import IProjectRepository


class RestoreProjectUseCase:
    def __init__(self, project_repository: IProjectRepository):
        self.project_repository = project_repository

    def execute(self, project_id: str) -> Project:
        project = self.project_repository.get_project_by_id(project_id)
        if not project:
            raise ValueError("Project not found")
        if not project.is_archived:
            raise ValueError("Project is not archived")
        project.restore()
        return project
