from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from src.salary.dependencies import get_salary_by_id
from src.auth.dependencies import get_current_user
from src.salary.schemas import SalaryOut
from src.auth.schemas import UserSchema

router = APIRouter(
    prefix="/salary",
    tags=["salary"],
)


@router.get("/", response_model=SalaryOut)
async def get_user_salary(current_user: Annotated[UserSchema, Depends(get_current_user)]) -> SalaryOut:
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await get_salary_by_id(current_user.salary_id)
