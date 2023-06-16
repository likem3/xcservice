from fastapi import APIRouter, status, Body
from fastapi.responses import JSONResponse
from users.schemas import UserCreate, UserInDB, UserPublic


router = APIRouter()


@router.post(
    "/create",
    tags=["user registration"],
    description="Register the user",
    response_model=UserPublic
)
async def user_create(user: UserCreate):
    return user