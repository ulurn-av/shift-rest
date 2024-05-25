import jwt
from datetime import datetime, timezone, timedelta

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.config import SECRET_KEY, ALGORITHM
from src.auth.security import verify_password
from src.database import get_async_session
from src.auth.models import User
from src.auth.schemas import UserIn, UserSchema

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token/")


async def get_user_by_id(user_id: int) -> UserSchema | None:
    async for session in get_async_session():
        return await session.scalar(select(User).options(joinedload(User.salary)).where(User.id == user_id))


async def get_user_by_username(username: str) -> UserSchema | None:
    async for session in get_async_session():
        return await session.scalar(select(User).where(User.username == username))


async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserSchema | None:
    if not token:
        return None
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    user_id: int = payload.get("sub")
    return await get_user_by_id(user_id)


async def authenticate_user(user_in: UserIn) -> UserSchema | None:
    user = await get_user_by_username(user_in.username)
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
