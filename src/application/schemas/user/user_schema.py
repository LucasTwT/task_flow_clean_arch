from pydantic import BaseModel, EmailStr, Field

from domain.models.user import User


class RegisterUserRequestSchema(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=User._PASSWORD_MIN_LENGTH, max_length=64)


class RegisterUserResponseSchema(BaseModel):
    id: str
    username: str
    email: str
    access_token: str
