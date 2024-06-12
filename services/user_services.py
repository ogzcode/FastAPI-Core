from sqlalchemy.orm import Session
from datetime import datetime
from models.user import User, UserResponseSchema, UserCreateSchema, UserUpdateSchema


class UserServices:
    @staticmethod
    def get_all_users(db: Session) -> list[UserResponseSchema]:
        users = db.query(User).all()
        return [UserResponseSchema(**user.dump()) for user in users]

    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> UserResponseSchema:
        user = db.query(User).filter(User.id == user_id).first()
        return UserResponseSchema(**user.dump()) if user else None

    @staticmethod
    def create_user(db: Session, user: UserCreateSchema) -> UserResponseSchema:
        new_user = User(**user)
        new_user.password = new_user.get_password_hash(new_user.password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return UserResponseSchema(**new_user.dump())

    @staticmethod
    def update_user(db: Session, user_id: int, user: UserUpdateSchema) -> UserResponseSchema:
        old_user = db.query(User).filter(User.id == user_id).first()

        for key, value in user.model_dump().items():
            if key == "password" and not old_user.verify_password(value):
                value = old_user.get_password_hash(value)
                setattr(old_user, key, value)
            elif key != "password" and value is not None and value != "":
                setattr(old_user, key, value)

        old_user.updated_at = datetime.now()

        db.commit()
        db.refresh(old_user)
        
        return UserResponseSchema(**old_user.dump())

    @staticmethod
    def delete_user(db: Session, user_id: int) -> bool:
        db.query(User).filter(User.id == user_id).delete()
        db.commit()
        return True

    @staticmethod
    def get_user_by_email(db: Session, email: str) -> UserResponseSchema:
        user = db.query(User).filter(User.email == email).first()
        return UserResponseSchema(**user.dump()) if user else None

    @staticmethod
    def user_is_login(db: Session, email: str, password: str) -> UserResponseSchema:
        user = db.query(User).filter(User.email == email).first()
        return UserResponseSchema(**user.dump()) if (user and user.verify_password(password)) else None

    @staticmethod
    def delete_all_users(db: Session) -> bool:
        db.query(User).delete()
        db.commit()
        return True
