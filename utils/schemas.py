from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing import TypeVar, Generic, Union, Dict

dinamic_data = TypeVar('dinamic_data')

class CustomResponse(GenericModel, Generic[dinamic_data]):
    message: str
    data: Union[dinamic_data, Dict]
    status: int


class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    token: str
    user: dict

class SignupRequest(BaseModel):
    username: str
    email: str
    password: str