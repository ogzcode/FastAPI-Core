from pydantic import BaseModel

class CustomResponse(BaseModel):
    message: str
    data: dict
    status: int


class Token(BaseModel):
    access_token: str

class TokenData(BaseModel):
    username: str = None
    email: str = None
    id: int = None


class LoginSchema(BaseModel):
    email: str
    password: str