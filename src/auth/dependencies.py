import jwt
from datetime import datetime, timezone, timedelta
from sqlalchemy import select

from src.config import SECRET_KEY, ALGORITHM
from src.auth.security import verify_password
from src.database import get_async_session
from src.auth.models import User


async def get_user_by_id(user_id: int) -> User | None:
    async for session in get_async_session():
        return await session.scalar(select(User).where(User.id == user_id))


async def get_user_by_name(username: str) -> User | None:
    async for session in get_async_session():
        return await session.scalar(select(User).where(User.name == username))


async def authenticate_user(username: str, password: str) -> User | bool:
    user = await get_user_by_name(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)