from uuid import uuid4

from application.schemas.project.project_schema import (
    ArchiveProjectRequestSchema,
    ArchiveProjectResponseSchema,
    CreateProjectRequestSchema,
    CreateProjectResponseSchema,
    ProjectResponseSchema,
)
from application.use_cases.project.archive_project import ArchiveProjectUseCase
from application.use_cases.project.create_project import CreateProjectInput, CreateProjectUseCase
from application.use_cases.project.list_user_projects import ListUserProjectsUseCase
from application.use_cases.project.restore_project import RestoreProjectUseCase


class CreateProjectController:
    def __init__(self, create_project_use_case: CreateProjectUseCase) -> None:
        self.create_project_use_case = create_project_use_case

    def create(self, payload: CreateProjectRequestSchema, owner_id: str) -> CreateProjectResponseSchema:
        project = self.create_project_use_case.execute(
            CreateProjectInput(id=str(uuid4()), name=payload.name, owner_id=owner_id, description=payload.description)
        )
        return CreateProjectResponseSchema(
            id=project.id,
            name=project.name,
            owner_id=project.owner_id,
            description=project.description,
            is_archived=project.is_archived,
        )


class ListUserProjectsController:
    def __init__(self, list_user_projects_use_case: ListUserProjectsUseCase) -> None:
        self.list_user_projects_use_case = list_user_projects_use_case

    def list(self, user_id: str) -> list[ProjectResponseSchema]:
        projects = self.list_user_projects_use_case.execute(user_id)
        return [
            ProjectResponseSchema(
                id=p.id,
                name=p.name,
                owner_id=p.owner_id,
                description=p.description,
                is_archived=p.is_archived,
            )
            for p in projects
        ]


class ArchiveProjectController:
    def __init__(self, archive_project_use_case: ArchiveProjectUseCase) -> None:
        self.archive_project_use_case = archive_project_use_case

    def archive(self, payload: ArchiveProjectRequestSchema) -> ArchiveProjectResponseSchema:
        project = self.archive_project_use_case.execute(payload.project_id)
        return ArchiveProjectResponseSchema(id=project.id, name=project.name, is_archived=project.is_archived)


class RestoreProjectController:
    def __init__(self, restore_project_use_case: RestoreProjectUseCase) -> None:
        self.restore_project_use_case = restore_project_use_case

    def restore(self, payload: ArchiveProjectRequestSchema) -> ArchiveProjectResponseSchema:
        project = self.restore_project_use_case.execute(payload.project_id)
        return ArchiveProjectResponseSchema(id=project.id, name=project.name, is_archived=project.is_archived)
