from fastapi import APIRouter, Depends, HTTPException
from services import user_services
from database.config import get_db
from database import schemas
from utils.schemas import CustomResponse, LoginSchema
from utils.auth import get_current_user, create_access_token, check_role

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/login/", response_model=CustomResponse)
def login_user(user: LoginSchema, db=Depends(get_db)):
    db_user = user_services.get_user_by_email(db, user.email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    user_hash_password = db_user.verify_password(user.password)

    if not user_hash_password:
        raise HTTPException(status_code=400, detail="Invalid password")

    access_token = create_access_token(id=db_user.id, role=db_user.role)
    response_user = schemas.User(**db_user.model_dump())

    return CustomResponse(
        message="User logged in successfully",
        data={
            "token": access_token,
            "user": response_user.model_dump()
        },
        status=200
    )


@router.get("/getUserById/{user_id}", response_model=CustomResponse, dependencies=[Depends(check_role("admin"))])
def read_user(user_id: int, db=Depends(get_db)):
    db_user = user_services.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return CustomResponse(
        message="User retrieved successfully",
        data={
            "user_id": user_id,
        },
        status=200
    )


@router.post("/createUser/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db=Depends(get_db)):
    try:
        db_user = user_services.get_user_by_email(db, user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        created_user = user_services.create_user(db, user)

        return created_user
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/updateUser/", response_model=schemas.User)
def update_user(user: schemas.UserBase, db=Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    db_user = user_services.get_user(db, current_user)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = user_services.update_user(current_user, db, user)

    return updated_user


@router.delete("/deleteUserById/{user_id}")
def delete_user(user_id: int, db=Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    print(current_user)

    db_user = user_services.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_services.delete_user(db, user_id)

    return {
        "message": "User deleted successfully"
    }


@router.get("/getUsers/", response_model=CustomResponse)
def read_users(db=Depends(get_db)):
    users = user_services.get_users(db)
    
    user_list = [schemas.User(**user.model_dump()) for user in users]

    return CustomResponse(
        message="Users retrieved successfully",
        data={
            "users": user_list
        },
        status=200
    )

@router.delete("/deleteAllUsers/", response_model=CustomResponse)
def delete_all_users(db=Depends(get_db)):
    user_services.delete_all_users(db)

    return CustomResponse(
        message="All users deleted successfully",
        status=200,
        data={}
    )