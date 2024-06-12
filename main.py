from routes import authRoutes, userRoutes
from core import db, exceptions
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()


db.create_tables()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(Exception,exceptions.http_500_error_handler)
app.add_exception_handler(HTTPException, exceptions.http_exception_handler)


app.include_router(authRoutes)
app.include_router(userRoutes)


@app.get("/", tags=["root"])
async def root():
    return {"message": "Hello World"}
