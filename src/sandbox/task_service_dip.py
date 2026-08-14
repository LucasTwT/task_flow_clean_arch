from dataclasses import dataclass
from datetime import datetime
from abc import ABC, abstractmethod
from typing_extensions import override

@dataclass
class TaskData:
    id: str
    title: str
    owner_id: str
    created_at: datetime | None = None

class ITaskRepository(ABC):
    @abstractmethod
    def save(self, task: TaskData) -> None:
        pass

    @abstractmethod
    def get_by_id(self, task_id: str) -> TaskData | None:
        pass

class PostgresTaskRepository(ITaskRepository):
    @override
    def save(self, task: TaskData) -> None:
        print(f"[PostgreSQL] Guardando tarea {task.id} en la base de datos...")

    @override
    def get_by_id(self, task_id: str) -> TaskData | None:
        print(f"[PostgreSQL] Buscando tarea {task_id} en la base de datos...")
        return None


class TaskService:
    repository: ITaskRepository

    def __init__(self, repository: ITaskRepository) -> None:
        self.repository = repository

    def create_task(self, task: TaskData) -> None:
        self.repository.save(task)

    def get_task(self, task_id: str) -> TaskData | None:
        return self.repository.get_by_id(task_id)
