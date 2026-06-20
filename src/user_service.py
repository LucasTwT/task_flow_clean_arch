import re
from dataclasses import dataclass
from typing import final


@dataclass
class UserData:
    id: str
    username: str
    email: str
    password: str

@final
class UserValidator:
    _PASSWORD_PATTERN = r".*."
    _EMAIL_PATTERN = r".*@+.*"
    _PASSWORD_MIN_LENGTH = 6

    def validate_email(self, email: str) -> bool:
        return True if re.fullmatch(pattern=self._EMAIL_PATTERN, string=email) else False

    def validate_password(self, password: str) -> bool:
        return True if (re.fullmatch(pattern=self._PASSWORD_PATTERN, string=password) and len(password) > self._PASSWORD_MIN_LENGTH) else False


class UserRepository:
    def __init__(self) -> None:
        self.users: list[UserData] = []

    def save_user(self, userdata: UserData) -> None:
        self.users.append(userdata)

    def get_user(self, id: str) -> UserData | None:
        for user in self.users:
            if user.id == id:
                return user
        return None


class UserNotifier:
    def send_email(self, email: str) -> None:
        print(f"Email enviado a {email}")
