from domain.models.user import User
from domain.ports.repositories import IUserRepository


class GetUserProfileUseCase:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: str) -> User | None:
        return self.user_repository.get_user(user_id)
