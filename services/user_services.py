from sqlalchemy.orm import Session
from database.models import User
from database import schemas


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(**user.model_dump())
    db_user.password = db_user.get_password_hash(user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(id: int, db: Session, user: schemas.UserBase):
    db_user = get_user(db, id)
    db_user.username = user.username
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    db.delete(db_user)
    db.commit()
    return db_user


def get_users(db: Session):
    return db.query(User).all()

def get_user_role(db: Session, id: int):
    return db.query(User).filter(User.id == id).first().role

def delete_all_users(db: Session):
    db.query(User).delete()
    db.commit()


