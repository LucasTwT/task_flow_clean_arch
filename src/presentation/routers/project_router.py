from fastapi import APIRouter, Depends

from application.schemas.project.project_schema import (
    ArchiveProjectRequestSchema,
    ArchiveProjectResponseSchema,
    CreateProjectRequestSchema,
    CreateProjectResponseSchema,
    ProjectResponseSchema,
)
from infrastructure.container import Container, get_container

router = APIRouter(tags=["projects"])


@router.post("/projects", response_model=CreateProjectResponseSchema)
def create_project(
    payload: CreateProjectRequestSchema,
    owner_id: str = "default-user",
    container: Container = Depends(get_container),
):
    return container.create_project_controller.create(payload, owner_id)


@router.get("/users/{user_id}/projects", response_model=list[ProjectResponseSchema])
def list_user_projects(
    user_id: str,
    container: Container = Depends(get_container),
):
    return container.list_user_projects_controller.list(user_id)


@router.post("/projects/archive", response_model=ArchiveProjectResponseSchema)
def archive_project(
    payload: ArchiveProjectRequestSchema,
    container: Container = Depends(get_container),
):
    return container.archive_project_controller.archive(payload)


@router.post("/projects/restore", response_model=ArchiveProjectResponseSchema)
def restore_project(
    payload: ArchiveProjectRequestSchema,
    container: Container = Depends(get_container),
):
    return container.restore_project_controller.restore(payload)
