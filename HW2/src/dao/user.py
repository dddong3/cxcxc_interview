from HW2.src.models.user import User, User_Pydantic, UserIn_Pydantic


class UserDao:
    @staticmethod
    async def get_all_users() -> list[User_Pydantic]:
        return await User_Pydantic.from_queryset(User.all())

    @staticmethod
    async def create_user(user: UserIn_Pydantic) -> User_Pydantic:
        user_obj = User(**user.dict())
        await user_obj.save()
        return await User_Pydantic.from_tortoise_orm(user_obj)
