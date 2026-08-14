from typing import override

from domain.models.project import Project
from domain.models.task import Task
from domain.models.user import User
from domain.ports.repositories import (
    IProjectRepository,
    ITaskReader,
    ITaskWriter,
    IUserRepository,
)


class UserRepository(IUserRepository):
    def __init__(self) -> None:
        self.users: list[User] = []

    @override
    def save_user(self, user: User) -> None:
        self.users.append(user)

    @override
    def get_user(self, id: str) -> User | None:
        for user in self.users:
            if user.id == id:
                return user
        return None

    @override
    def exists_by_email(self, email: str) -> bool:
        return any(user.email == email for user in self.users)


class ProjectRepository(IProjectRepository):    
    def __init__(self) -> None:
        self.projects: list[Project] = []
    
    @override
    def save_project(self, project: Project) -> None:
        self.projects.append(project)

    @override
    def get_projects(self, user_id: str) -> list[Project]:
        return [project for project in self.projects if project.owner_id == user_id]
    
    @override
    def get_project_by_id(self, project_id: str) -> Project | None:
        for project in self.projects:
            if project.id == project_id:
                return project
        return None

    @override
    def exists_by_name(self, name: str) -> bool:
        return any(project.name == name for project in self.projects)


class TaskRepository(ITaskReader, ITaskWriter):
    def __init__(self) -> None:
        self.tasks: list[Task] = []

    @override
    def save_task(self, task: Task) -> None:
        self.tasks.append(task)

    @override
    def update_task(self, task: Task) -> None:
        for i, t in enumerate(self.tasks):
            if t.id == task.id:
                self.tasks[i] = task
                return

    @override
    def get_task_by_project_id(self, project_id: str) -> list[Task]:
        return [task for task in self.tasks if task.get_project_id() == project_id]

    @override
    def get_task_by_id(self, task_id: str) -> Task | None:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    @override
    def get_tasks_by_user_id(self, user_id: str) -> list[Task]:
        return [task for task in self.tasks if task.get_owner_id() == user_id]

    @override
    def get_tasks_by_assigned_user(self, user_id: str) -> list[Task]:
        return [task for task in self.tasks if task.get_assigned_to() == user_id]
