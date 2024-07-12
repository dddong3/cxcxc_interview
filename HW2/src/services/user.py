from HW2.src.dao.user import UserDao
from HW2.src.models.user import User_Pydantic, UserIn_Pydantic


class UserService:
    def __init__(self):
        self.dao = UserDao()

    async def get_all_users(self) -> list[User_Pydantic]:
        return await self.dao.get_all_users()

    async def create_user(self, user: UserIn_Pydantic) -> User_Pydantic:
        return await self.dao.create_user(user)
