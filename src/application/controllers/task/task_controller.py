from uuid import uuid4

from application.schemas.task.task_schema import (
    CompleteTaskResponseSchema,
    CreateTaskRequestSchema,
    CreateTaskResponseSchema,
    TaskIdRequestSchema,
    TaskResponseSchema,
)
from application.use_cases.task.complete_task import CompleteTaskUseCase
from application.use_cases.task.create_task import CreateTaskInput, CreateTaskUseCase
from application.use_cases.task.get_user_tasks import GetUserTasksUseCase
from application.use_cases.task.list_project_tasks import ListProjectTasksUseCase
from application.use_cases.task.reopen_task import ReopenTaskUseCase


class CreateTaskController:
    def __init__(self, create_task_use_case: CreateTaskUseCase) -> None:
        self.create_task_use_case = create_task_use_case

    def create(self, payload: CreateTaskRequestSchema, owner_id: str) -> CreateTaskResponseSchema:
        task = self.create_task_use_case.execute(
            CreateTaskInput(
                id=str(uuid4()),
                task_name=payload.task_name,
                project_id=payload.project_id,
                owner_id=owner_id,
            )
        )
        return CreateTaskResponseSchema(
            id=task.id,
            task_name=task.get_task_name(),
            project_id=task.get_project_id(),
            status=task.get_status(),
        )


class ListProjectTasksController:
    def __init__(self, list_project_tasks_use_case: ListProjectTasksUseCase) -> None:
        self.list_project_tasks_use_case = list_project_tasks_use_case

    def list(self, project_id: str) -> list[TaskResponseSchema]:
        tasks = self.list_project_tasks_use_case.execute(project_id)
        return [
            TaskResponseSchema(
                id=t.id,
                task_name=t.get_task_name(),
                project_id=t.get_project_id(),
                assigned_to=t.get_assigned_to(),
                status=t.get_status(),
            )
            for t in tasks
        ]


class CompleteTaskController:
    def __init__(self, complete_task_use_case: CompleteTaskUseCase) -> None:
        self.complete_task_use_case = complete_task_use_case

    def complete(self, payload: TaskIdRequestSchema) -> CompleteTaskResponseSchema:
        task = self.complete_task_use_case.execute(payload.task_id)
        return CompleteTaskResponseSchema(id=task.id, task_name=task.get_task_name(), status=task.get_status())


class ReopenTaskController:
    def __init__(self, reopen_task_use_case: ReopenTaskUseCase) -> None:
        self.reopen_task_use_case = reopen_task_use_case

    def reopen(self, payload: TaskIdRequestSchema) -> CompleteTaskResponseSchema:
        task = self.reopen_task_use_case.execute(payload.task_id)
        return CompleteTaskResponseSchema(id=task.id, task_name=task.get_task_name(), status=task.get_status())


class GetUserTasksController:
    def __init__(self, get_user_tasks_use_case: GetUserTasksUseCase) -> None:
        self.get_user_tasks_use_case = get_user_tasks_use_case

    def list(self, user_id: str) -> list[TaskResponseSchema]:
        tasks = self.get_user_tasks_use_case.execute(user_id)
        return [
            TaskResponseSchema(
                id=t.id,
                task_name=t.get_task_name(),
                project_id=t.get_project_id(),
                assigned_to=t.get_assigned_to(),
                status=t.get_status(),
            )
            for t in tasks
        ]
