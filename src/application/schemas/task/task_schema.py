from pydantic import BaseModel

from domain.models.user import User


class CreateTaskRequestSchema(BaseModel):
    task_name: str
    project_id: str


class CreateTaskResponseSchema(BaseModel):
    id: str
    task_name: str
    project_id: str
    status: bool


class TaskResponseSchema(BaseModel):
    id: str
    task_name: str
    project_id: str
    assigned_to: str | None
    status: bool


class TaskIdRequestSchema(BaseModel):
    task_id: str


class CompleteTaskResponseSchema(BaseModel):
    id: str
    task_name: str
    status: bool


class AssignTaskRequestSchema(BaseModel):
    task_id: str
    user_id: str


class AssignTaskResponseSchema(BaseModel):
    task_id: str
    task_name: str
    assigned_to: str
    status: bool
