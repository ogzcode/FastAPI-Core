from datetime import datetime
from passlib.context import CryptContext
from sqlalchemy import Column, Integer, String

from core import db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(db.Base):
    """ User model"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String, default="user")
    created_at = Column(String, default=datetime.now())
    updated_at = Column(String, default=datetime.now())

    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.password)

    def get_password_hash(self, password):
        """ Hash the password using bcrypt """
        return pwd_context.hash(password)

    def __repr__(self):
        return f"<User {self.username}>"

    def dump(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)
        }
