from pydantic import BaseModel
from enum import Enum

class Role(str, Enum):
    user = "user"
    admin = "admin"

class UserBase(BaseModel):
    username: str
    email: str
    role: Role

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True