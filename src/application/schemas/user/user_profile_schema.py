from pydantic import BaseModel


class GetUserProfileResponseSchema(BaseModel):
    id: str
    username: str
    email: str
