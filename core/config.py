from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from typing import Generator

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

class Database:
    def __init__(self):
        self.engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
        self.Base = declarative_base()
        self.session = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine)

    def create_tables(self):
        self.Base.metadata.create_all(bind=self.engine)

    def get_session(self) -> Generator[Session, None, None]:
        session = self.session()

        try:
            yield session
        finally:
            session.close()
