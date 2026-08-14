from repositories import UserRepository, ProjectRepository, TaskRepository
from notifiers import EmailNotifier

from application.use_cases.user.register_user import RegisterUserUseCase
from application.use_cases.user.get_user_profile import GetUserProfileUseCase
from application.use_cases.project.create_project import CreateProjectUseCase
from application.use_cases.project.list_user_projects import ListUserProjectsUseCase
from application.use_cases.project.archive_project import ArchiveProjectUseCase
from application.use_cases.project.restore_project import RestoreProjectUseCase
from application.use_cases.task.create_task import CreateTaskUseCase
from application.use_cases.task.list_project_tasks import ListProjectTasksUseCase
from application.use_cases.task.complete_task import CompleteTaskUseCase
from application.use_cases.task.reopen_task import ReopenTaskUseCase
from application.use_cases.task.assign_task import AssignTaskUseCase
from application.use_cases.task.get_user_tasks import GetUserTasksUseCase

from application.controllers.user.user_controller import UserController
from application.controllers.user.user_profile_controller import GetUserProfileController
from application.controllers.project.project_controller import (
    CreateProjectController,
    ListUserProjectsController,
    ArchiveProjectController,
    RestoreProjectController,
)
from application.controllers.task.task_controller import (
    CreateTaskController,
    ListProjectTasksController,
    CompleteTaskController,
    ReopenTaskController,
    GetUserTasksController,
)
from application.controllers.task.assign_task_controller import AssignTaskController


class Container:
    """Wires all dependencies together — one place to rule them all."""

    def __init__(self) -> None:
        # --- Repositories ---
        self.user_repo = UserRepository()
        self.project_repo = ProjectRepository()
        self.task_repo = TaskRepository()
        self.notifier = EmailNotifier()

        # --- Use Cases ---
        self.register_user_uc = RegisterUserUseCase(self.user_repo)
        self.get_user_profile_uc = GetUserProfileUseCase(self.user_repo)
        self.create_project_uc = CreateProjectUseCase(self.project_repo)
        self.list_user_projects_uc = ListUserProjectsUseCase(self.project_repo)
        self.archive_project_uc = ArchiveProjectUseCase(self.project_repo)
        self.restore_project_uc = RestoreProjectUseCase(self.project_repo)
        self.create_task_uc = CreateTaskUseCase(self.task_repo, self.project_repo)
        self.list_project_tasks_uc = ListProjectTasksUseCase(self.task_repo, self.project_repo)
        self.complete_task_uc = CompleteTaskUseCase(self.task_repo, self.task_repo)
        self.reopen_task_uc = ReopenTaskUseCase(self.task_repo, self.task_repo)
        self.assign_task_uc = AssignTaskUseCase(self.task_repo, self.user_repo, self.task_repo, self.notifier)
        self.get_user_tasks_uc = GetUserTasksUseCase(self.task_repo)

        # --- Controllers ---
        self.user_controller = UserController(self.register_user_uc)
        self.profile_controller = GetUserProfileController(self.get_user_profile_uc)
        self.create_project_controller = CreateProjectController(self.create_project_uc)
        self.list_user_projects_controller = ListUserProjectsController(self.list_user_projects_uc)
        self.archive_project_controller = ArchiveProjectController(self.archive_project_uc)
        self.restore_project_controller = RestoreProjectController(self.restore_project_uc)
        self.create_task_controller = CreateTaskController(self.create_task_uc)
        self.list_project_tasks_controller = ListProjectTasksController(self.list_project_tasks_uc)
        self.complete_task_controller = CompleteTaskController(self.complete_task_uc)
        self.reopen_task_controller = ReopenTaskController(self.reopen_task_uc)
        self.assign_task_controller = AssignTaskController(self.assign_task_uc)
        self.get_user_tasks_controller = GetUserTasksController(self.get_user_tasks_uc)


_container: Container | None = None


def get_container() -> Container:
    global _container
    if _container is None:
        _container = Container()
    return _container
