from sqlalchemy import select

from src.salary.models import Salary
from src.salary.schemas import SalaryOut
from src.database import get_async_session


async def get_salary_by_id(salary_id: int) -> SalaryOut | None:
    async for session in get_async_session():
        return await session.scalar(select(Salary).where(Salary.id == salary_id))
