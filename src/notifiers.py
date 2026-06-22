from abc import ABC, abstractmethod

from typing_extensions import override

class UserNotifier(ABC):
    @abstractmethod
    def send(self, to: str, message: str) -> None: ...


class EmailNotifier(UserNotifier):
    @override
    def send(self, to: str, message: str) -> None:
        print(f"Email a {to}: {message}")


class SMSNotifier(UserNotifier):
    @override
    def send(self, to: str, message: str) -> None:
        print(f"SMS a {to}: {message}")


class PushNotifier(UserNotifier):
    @override
    def send(self, to: str, message: str) -> None:
        print(f"Push a {to}: {message}")
