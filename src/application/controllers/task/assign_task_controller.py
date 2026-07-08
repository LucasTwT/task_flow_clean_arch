from application.schemas.task.task_schema import AssignTaskRequestSchema, AssignTaskResponseSchema
from application.use_cases.task.assign_task import AssignTaskUseCase


class AssignTaskController:
    def __init__(self, assign_task_use_case: AssignTaskUseCase):
        self.assign_task_use_case = assign_task_use_case

    def assign_task(self, payload: AssignTaskRequestSchema) -> AssignTaskResponseSchema:
        task = self.assign_task_use_case.execute(task_id=payload.task_id, user_id=payload.user_id)
        if task.get_assigned_to() != payload.user_id:
            raise ValueError("La tarea no fue asignada correctamente")
        return AssignTaskResponseSchema(task_id=task.id, task_name=task.get_task_name(), assigned_to=task.get_assigned_to(), status=True)
