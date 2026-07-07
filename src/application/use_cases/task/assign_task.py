from models.task_entity import Task
from models.user import User
from repositories import ITaskRepository, IUserRepository
from notifiers import UserNotifier


class AssignTaskUseCase:
    def __init__(
        self,
        task_repository: ITaskRepository,
        user_repository: IUserRepository,
        notifier: UserNotifier,
    ) -> None:
        self.task_repository = task_repository
        self.user_repository = user_repository
        self.notifier = notifier

    def execute(self, task_id: str, user_id: str) -> Task:
        task = self.task_repository.get_task_by_id(task_id)
        if not task:
            raise ValueError("La tarea no existe")

        user = self.user_repository.get_user(user_id)
        if not user:
            raise ValueError("El usuario no existe")

        task.assign_to(user_id)
        self.task_repository.update_task(task)

        self.notifier.send(
            to=user.email,
            message=f"Se te ha asignado la tarea: {task._task_name}",
        )

        return task
