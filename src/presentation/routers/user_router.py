from fastapi import APIRouter, Depends

from application.schemas.user.user_schema import RegisterUserRequestSchema, RegisterUserResponseSchema
from application.schemas.user.user_profile_schema import GetUserProfileResponseSchema
from presentation.container import Container, get_container

router = APIRouter(tags=["users"])


@router.post("/users", response_model=RegisterUserResponseSchema)
def register_user(
    payload: RegisterUserRequestSchema,
    container: Container = Depends(get_container),
):
    return container.user_controller.register(payload)


@router.get("/users/{user_id}", response_model=GetUserProfileResponseSchema)
def get_user_profile(
    user_id: str,
    container: Container = Depends(get_container),
):
    return container.profile_controller.get(user_id)
