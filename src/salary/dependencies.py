import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select

from src.auth.dependencies import get_user_by_id
from src.auth.models import User
from src.auth.schemas import UserOut
from src.salary.models import Salary
from src.salary.schemas import SalaryOut
from src.config import ALGORITHM, SECRET_KEY
from src.database import get_async_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token/")


async def get_salary_by_id(username: int) -> SalaryOut | None:
    async for session in get_async_session():
        return await session.scalar(select(Salary).where(User.id == username))


async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserOut | None:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username: int = payload.get("sub")
    return await get_user_by_id(username)
