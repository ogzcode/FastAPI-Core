from sqlalchemy import Column, Integer, String
from passlib.context import CryptContext
from .config import Base
from .schemas import Role
from enum import Enum

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String, default=Role.user.value)

    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.password)
    
    def get_password_hash(self, password):
        return pwd_context.hash(password)
    
    def model_dump(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role
        }

