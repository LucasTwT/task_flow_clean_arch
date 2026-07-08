from pydantic import BaseModel

from application.use_cases.user.get_user_profile import GetUserProfileUseCase


class GetUserProfileResponseSchema(BaseModel):
    id: str
    username: str
    email: str


class GetUserProfileController:
    def __init__(self, get_user_profile_use_case: GetUserProfileUseCase) -> None:
        self.get_user_profile_use_case = get_user_profile_use_case

    def get(self, user_id: str) -> GetUserProfileResponseSchema:
        user = self.get_user_profile_use_case.execute(user_id)
        if not user:
            raise ValueError("Usuario no encontrado")
        return GetUserProfileResponseSchema(id=user.id, username=user.username, email=user.email)
