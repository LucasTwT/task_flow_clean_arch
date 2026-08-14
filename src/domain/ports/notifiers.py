from abc import ABC, abstractmethod


class UserNotifier(ABC):
    @abstractmethod
    def send(self, to: str, message: str) -> None: ...
