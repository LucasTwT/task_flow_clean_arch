from dataclasses import dataclass

from domain.models.user import User
from domain.ports.repositories import IUserRepository

@dataclass
class RegisterUserInput:
    id: str
    username: str
    email: str
    password: str


class RegisterUserUseCase:
    def __init__(self, user_repository: IUserRepository) -> None:
        self.user_repository = user_repository

    def execute(self, input: RegisterUserInput) -> User:
        if self.user_repository.exists_by_email(input.email):
            raise ValueError(f"Ya existe un usuario con el email {input.email}")

        user = User(
            id=input.id,
            username=input.username,
            email=input.email,
            password=input.password,
        )
        self.user_repository.save_user(user)
        return user
