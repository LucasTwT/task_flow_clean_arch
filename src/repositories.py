from models.user import User


class UserRepository:
    def __init__(self) -> None:
        self.users: list[User] = []

    def save_user(self, user: User) -> None:
        self.users.append(user)

    def get_user(self, id: str) -> User | None:
        for user in self.users:
            if user.id == id:
                return user
        return None
