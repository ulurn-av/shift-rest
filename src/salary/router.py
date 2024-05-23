from typing import Annotated

from fastapi import APIRouter, Depends

from src.salary.dependencies import get_current_user, get_salary_by_id
from src.salary.schemas import SalaryOut
from src.auth.schemas import UserOut

router = APIRouter(
    prefix="/salary",
    tags=["salary"],
)


@router.get("/", response_model=SalaryOut)
async def get_user_salary(current_user: Annotated[UserOut, Depends(get_current_user)]):
    return await get_salary_by_id(current_user.salary_id)
