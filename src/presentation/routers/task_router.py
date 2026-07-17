from fastapi import APIRouter, Depends

from application.schemas.task.task_schema import (
    AssignTaskRequestSchema,
    AssignTaskResponseSchema,
    CompleteTaskResponseSchema,
    CreateTaskRequestSchema,
    CreateTaskResponseSchema,
    TaskIdRequestSchema,
    TaskResponseSchema,
)
from presentation.container import Container, get_container

router = APIRouter(tags=["tasks"])


@router.post("/tasks", response_model=CreateTaskResponseSchema, status_code=201)
def create_task(
    payload: CreateTaskRequestSchema,
    owner_id: str = "default-user",
    container: Container = Depends(get_container),
):
    return container.create_task_controller.create(payload, owner_id)


@router.get("/projects/{project_id}/tasks", response_model=list[TaskResponseSchema])
def list_project_tasks(
    project_id: str,
    container: Container = Depends(get_container),
):
    return container.list_project_tasks_controller.list(project_id)


@router.post("/tasks/complete", response_model=CompleteTaskResponseSchema)
def complete_task(
    payload: TaskIdRequestSchema,
    container: Container = Depends(get_container),
):
    return container.complete_task_controller.complete(payload)


@router.post("/tasks/reopen", response_model=CompleteTaskResponseSchema)
def reopen_task(
    payload: TaskIdRequestSchema,
    container: Container = Depends(get_container),
):
    return container.reopen_task_controller.reopen(payload)


@router.post("/tasks/assign", response_model=AssignTaskResponseSchema)
def assign_task(
    payload: AssignTaskRequestSchema,
    container: Container = Depends(get_container),
):
    return container.assign_task_controller.assign_task(payload)


@router.get("/users/{user_id}/tasks", response_model=list[TaskResponseSchema])
def get_user_tasks(
    user_id: str,
    container: Container = Depends(get_container),
):
    return container.get_user_tasks_controller.list(user_id)
