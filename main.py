from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.config import engine
from database import models
from routes import users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}

