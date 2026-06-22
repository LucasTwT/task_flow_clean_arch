from dataclasses import dataclass

@dataclass
class UserData:
    id: str
    username: str
    email: str
    password: str

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
