from fastapi import APIRouter, HTTPException
from HW2.src.models.user import User_Pydantic, UserIn_Pydantic
from HW2.src.services.user import UserService

router = APIRouter(prefix="/user")
service = UserService()


@router.get("", response_model=list[User_Pydantic])
async def get_all_users():
    return await service.get_all_users()


@router.post("", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    return await service.create_user(user)
