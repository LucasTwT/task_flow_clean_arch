from models.user import User
from repositories import IUserRepository


class GetUserProfileUseCase:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: str) -> User | None:
        return self.user_repository.get_user(user_id)
