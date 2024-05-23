from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from datetime import timedelta

from src.auth.schemas import Token
from src.config import ACCESS_TOKEN_EXPIRE_MINUTES
from src.auth.dependencies import authenticate_user, create_access_token
from src.auth.schemas import UserIn

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    user_in = UserIn(username=form_data.username, password=form_data.password)
    user = await authenticate_user(user_in)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.id}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
