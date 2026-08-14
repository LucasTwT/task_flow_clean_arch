from typing_extensions import override

from domain.ports.notifiers import UserNotifier


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
