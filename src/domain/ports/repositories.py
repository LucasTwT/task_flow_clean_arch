from abc import ABC, abstractmethod

from domain.models.project import Project
from domain.models.task import Task
from domain.models.user import User


class IUserRepository(ABC):
    @abstractmethod
    def save_user(self, user: User) -> None: ...

    @abstractmethod
    def get_user(self, id: str) -> User | None: ...

    @abstractmethod
    def exists_by_email(self, email: str) -> bool: ...

class IProjectRepository(ABC):
    @abstractmethod
    def save_project(self, project: Project) -> None: ...

    @abstractmethod
    def get_projects(self, user_id: str) -> list[Project]: ...
    
    @abstractmethod
    def get_project_by_id(self, project_id: str) -> Project | None: ...

    @abstractmethod
    def exists_by_name(self, name: str) -> bool: ...

class ITaskReader(ABC):
    @abstractmethod
    def get_task_by_project_id(self, project_id: str) -> list[Task]: ...

    @abstractmethod
    def get_task_by_id(self, task_id: str) -> Task | None: ...

    @abstractmethod
    def get_tasks_by_user_id(self, user_id: str) -> list[Task]: ...

    @abstractmethod
    def get_tasks_by_assigned_user(self, user_id: str) -> list[Task]: ...


class ITaskWriter(ABC):
    @abstractmethod
    def save_task(self, task: Task) -> None: ...

    @abstractmethod
    def update_task(self, task: Task) -> None: ...

