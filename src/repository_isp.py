from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass
class TaskDTO:
    id: str
    title: str
    description: str
    owner_id: str
    is_completed: bool = False
    is_archived: bool = False
    created_at: datetime | None = None


class ITaskReader(ABC):
    """Solo lectura — 6 métodos relacionados."""

    @abstractmethod
    def get_by_id(self, task_id: str) -> TaskDTO | None: ...

    @abstractmethod
    def get_all_by_owner(self, owner_id: str) -> list[TaskDTO]: ...

    @abstractmethod
    def get_completed(self) -> list[TaskDTO]: ...

    @abstractmethod
    def get_pending(self) -> list[TaskDTO]: ...

    @abstractmethod
    def search_by_title(self, query: str) -> list[TaskDTO]: ...

    @abstractmethod
    def count_by_owner(self, owner_id: str) -> int: ...


class ITaskWriter(ABC):
    """Solo escritura — 5 métodos relacionados."""

    @abstractmethod
    def save(self, task: TaskDTO) -> None: ...

    @abstractmethod
    def update(self, task: TaskDTO) -> None: ...

    @abstractmethod
    def delete(self, task_id: str) -> None: ...

    @abstractmethod
    def mark_completed(self, task_id: str) -> None: ...

    @abstractmethod
    def mark_pending(self, task_id: str) -> None: ...


class ITaskArchiver(ABC):
    """Solo archivado — 4 métodos relacionados."""

    @abstractmethod
    def archive(self, task_id: str) -> None: ...

    @abstractmethod
    def restore(self, task_id: str) -> None: ...

    @abstractmethod
    def get_archived(self) -> list[TaskDTO]: ...

    @abstractmethod
    def purge_archived(self, days_old: int) -> int: ...


class InMemoryTaskReader(ITaskReader):
    """Implementa SOLO ITaskReader — no tiene métodos de escritura ni archivado."""

    def __init__(self, tasks: list[TaskDTO] | None = None) -> None:
        self._tasks = tasks or []

    def get_by_id(self, task_id: str) -> TaskDTO | None:
        for t in self._tasks:
            if t.id == task_id:
                return t
        return None

    def get_all_by_owner(self, owner_id: str) -> list[TaskDTO]:
        return [t for t in self._tasks if t.owner_id == owner_id]

    def get_completed(self) -> list[TaskDTO]:
        return [t for t in self._tasks if t.is_completed]

    def get_pending(self) -> list[TaskDTO]:
        return [t for t in self._tasks if not t.is_completed]

    def search_by_title(self, query: str) -> list[TaskDTO]:
        return [t for t in self._tasks if query.lower() in t.title.lower()]

    def count_by_owner(self, owner_id: str) -> int:
        return len(self.get_all_by_owner(owner_id))
