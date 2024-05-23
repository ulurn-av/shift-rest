import jwt
from datetime import datetime, timezone, timedelta
from sqlalchemy import select

from src.config import SECRET_KEY, ALGORITHM
from src.auth.security import verify_password
from src.database import get_async_session
from src.auth.models import User
from src.auth.schemas import UserIn, UserOut


async def get_user_by_id(user_id: int) -> UserOut | None:
    async for session in get_async_session():
        return await session.scalar(select(User).where(User.id == user_id))


async def get_user_by_name(username: str) -> UserOut | None:
    async for session in get_async_session():
        return await session.scalar(select(User).where(User.name == username))


async def authenticate_user(user_in: UserIn) -> UserOut | None:
    user = await get_user_by_name(user_in.username)
    if not user:
        return None
    if not verify_password(user_in.password, user.hashed_password):
        return None
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
