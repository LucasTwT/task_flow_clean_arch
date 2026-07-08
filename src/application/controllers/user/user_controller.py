from uuid import uuid4

from application.schemas.user.user_schema import RegisterUserRequestSchema, RegisterUserResponseSchema
from application.use_cases.user.register_user import RegisterUserInput, RegisterUserUseCase


class UserController:
    def __init__(self, register_user_use_case: RegisterUserUseCase) -> None:
        self.register_user_use_case = register_user_use_case

    def register(self, payload: RegisterUserRequestSchema) -> RegisterUserResponseSchema:
        user = self.register_user_use_case.execute(
            RegisterUserInput(
                id=str(uuid4()),
                username=payload.username,
                email=payload.email,
                password=payload.password,
            )
        )
        return RegisterUserResponseSchema(
            id=user.id,
            username=user.username,
            email=user.email,
            access_token="not implemented",
        )
