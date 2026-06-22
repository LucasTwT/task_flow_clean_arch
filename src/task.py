from abc import ABC, abstractmethod
from typing import override


class Task(ABC):
    def __init__(self, task_name: str) -> None:
        self._task_name = task_name
        self._status: bool = False

    def finish(self) -> None:
        self._status = True

    @abstractmethod
    def get_task_info(self) -> str: ...


class RecurringTask(Task):
    def __init__(self, task_name: str, interval: int) -> None:
        super().__init__(task_name)
        self._interval = interval

    @override
    def get_task_info(self) -> str:
        return f"Tarea recurrente: {self._task_name}, cada {self._interval} días |{'☑' if self._status else '☒'}|"


class MilestoneTask(Task):
    def __init__(self, task_name: str, milestone: str) -> None:
        super().__init__(task_name)
        self._milestone = milestone

    @override
    def get_task_info(self) -> str:
        return f"Hito: {self._task_name}, meta: {self._milestone} |{'☑' if self._status else '☒'}|"
