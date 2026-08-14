class Task:
    def __init__(self, id: str, task_name: str, project_id: str, owner_id: str):
        if not id:
            raise ValueError("El ID no puede estar vacío")
        if not task_name or not task_name.strip():
            raise ValueError("El nombre no puede estar vacío")
        if not project_id:
            raise ValueError("La tarea debe pertenecer a un proyecto")
        if not owner_id:
            raise ValueError("La tarea debe tener un creador")

        self.id = id
        self._task_name = task_name.strip()
        self._project_id = project_id
        self._owner_id = owner_id
        self._assigned_to: str | None = None
        self._status: bool = False
    
    def get_owner_id(self) -> str:
        return self._owner_id
    
    def get_project_id(self) -> str:
        return self._project_id
    
    def get_assigned_to(self) -> str | None:
        return self._assigned_to

    def get_status(self) -> bool:
        return self._status
    
    def get_task_name(self) -> str:
        return self._task_name

    def complete(self) -> None:
        self._status = True

    def reopen(self) -> None:
        self._status = False

    def assign_to(self, user_id: str) -> None:
        self._assigned_to = user_id
