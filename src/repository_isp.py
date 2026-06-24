from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    id: str
    title: str
    description: str
    owner_id: str
    is_completed: bool = False
    is_archived: bool = False
    created_at: datetime | None = None

class ITaskReader(ABC): 
    # --- Lectura ---
    @abstractmethod
    def get_by_id(self, task_id: str) -> Task | None: ...

    @abstractmethod
    def get_all_by_owner(self, owner_id: str) -> list[Task]: ...

    @abstractmethod
    def get_completed(self) -> list[Task]: ...

    @abstractmethod
    def get_pending(self) -> list[Task]: ...

    @abstractmethod
    def search_by_title(self, query: str) -> list[Task]: ...

    @abstractmethod
    def count_by_owner(self, owner_id: str) -> int: ...

class ITaskWriter(ABC):
    # --- Escritura ---
    @abstractmethod
    def save(self, task: Task) -> None: ...

    @abstractmethod
    def update(self, task: Task) -> None: ...

    @abstractmethod
    def delete(self, task_id: str) -> None: ...

    @abstractmethod
    def mark_completed(self, task_id: str) -> None: ...

    @abstractmethod
    def mark_pending(self, task_id: str) -> None: ...

class ITaskArchiver(ABC):
    # --- Archivado ---
    @abstractmethod
    def archive(self, task_id: str) -> None: ...

    @abstractmethod
    def restore(self, task_id: str) -> None: ...

    @abstractmethod
    def get_archived(self) -> list[Task]: ...

    @abstractmethod
    def purge_archived(self, days_old: int) -> int: ...
