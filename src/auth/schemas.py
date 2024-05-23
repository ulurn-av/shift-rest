from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class UserIn(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    username: str
    email: str
    name: str
    middle_name: str
    last_name: str

class UserSchema(UserOut):
    id: int
    hashed_password: str
    salary_id: int
