from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services import UserServices
from models.user import UserResponseSchema, UserUpdateSchema
from utils import CustomResponse
from core import db
from auth import authentication_service, authorization_service

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/getAll", response_model=CustomResponse[UserResponseSchema])
async def get_all_users(db: Session = Depends(db.get_session)):

    users = UserServices.get_all_users(db)
    return CustomResponse(
        message="Users retrieved successfully",
        data={
            "users": users
        },
        status=200
    )


@router.get("/getAllForAdmins", response_model=CustomResponse[UserResponseSchema])
async def get_all_users_for_admins(db: Session = Depends(db.get_session), current_user=Depends(authorization_service.check_role("admin"))):

    users = UserServices.get_all_users(db)
    return CustomResponse(
        message="Users retrieved successfully",
        data={
            "users": users
        },
        status=200
    )


@router.get("/getAllForAuth", response_model=CustomResponse[UserResponseSchema])
async def get_all_users_for_auth(db: Session = Depends(db.get_session), current_user: dict = Depends(authentication_service.get_current_user)):

    users = UserServices.get_all_users(db)
    return CustomResponse(
        message="Users retrieved successfully",
        data={
            "users": users
        },
        status=200
    )


@router.delete("/deleteAll", response_model=CustomResponse)
async def delete_all_users(db: Session = Depends(db.get_session)):

    UserServices.delete_all_users(db)
    return CustomResponse(
        message="Users deleted successfully",
        data={},
        status=200
    )


@router.put("/update/{id}", response_model=CustomResponse[UserResponseSchema])
async def update_user(id: int, user: UserUpdateSchema, db: Session = Depends(db.get_session)):
    if not UserServices.get_user_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    updated_user = UserServices.update_user(db, id, user)

    return CustomResponse(
        message="User updated successfully",
        data={
            "user": updated_user.model_dump()
        },
        status=200
    )
