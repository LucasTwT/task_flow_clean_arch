from models.task_entity import Task
from repositories import ITaskReader, ITaskWriter


class ReopenTaskUseCase:
    def __init__(
        self,
        task_repository: ITaskReader,
        task_writer: ITaskWriter,
    ) -> None:
        self.task_repository = task_repository
        self.task_writer = task_writer

    def execute(self, task_id: str) -> Task:
        task = self.task_repository.get_task_by_id(task_id)
        if not task:
            raise ValueError("La tarea no existe")
        if not task.get_status():
            raise ValueError("La tarea no está completada — no se puede reabrir")
        task.reopen()
        self.task_writer.update_task(task)
        return task
