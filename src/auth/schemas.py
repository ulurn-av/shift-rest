from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserOUT(BaseModel):
    username: str
    email: str
    name: str
    middle_name: str
    last_name: str
    salary_id: int