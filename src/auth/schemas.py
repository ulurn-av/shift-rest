from pydantic import BaseModel

from src.salary.schemas import SalaryOut


class Token(BaseModel):
    access_token: str
    token_type: str


class UserIn(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    username: str
    email: str
    name: str | None
    middle_name: str | None
    last_name: str | None
    salary: SalaryOut

    class Config:
        from_attributes = True


class UserSchema(UserOut):
    id: int
    salary_id: int
    hashed_password: str

    class Config:
        from_attributes = True
