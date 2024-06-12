from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    username: str
    email: str

    class Config:
        from_attribute = True

class UserCreateSchema(UserSchema):
    password: str

class UserUpdateSchema(UserSchema):
    password: str
    role: Optional[str] = None

class UserResponseSchema(UserSchema):
    id: int
    username: str
    email: str
    role: str
    created_at: str
    updated_at: str