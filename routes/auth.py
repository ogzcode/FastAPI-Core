from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services import UserServices
from core import db
from auth import token_service
from utils import CustomResponse, LoginRequest, LoginResponse, SignupRequest


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/login", response_model=CustomResponse[LoginResponse])
async def login(request: LoginRequest, db: Session = Depends(db.get_session)):

    user = UserServices.user_is_login(db, request.email, request.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = token_service.create_access_token(data={
        "sub": str(user.id),
        "email": user.email,
        "role": user.role
    })

    return CustomResponse(
        message="Login successful",
        data={"token": token, "user": user.model_dump()},
        status=200
    )


@router.post("/signup", response_model=CustomResponse)
async def signup(request: SignupRequest, db: Session = Depends(db.get_session)):

    user = UserServices.get_user_by_email(db, request.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    new_user = UserServices.create_user(db, request.model_dump())

    return CustomResponse(
        message="User created successfully",
        data={
            "user": new_user.dict()
        },
        status=201
    )
