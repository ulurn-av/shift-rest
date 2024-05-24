import asyncio
from datetime import date

from src.auth.security import get_password_hash
from src.database import get_async_session
from src.auth.models import User
from src.salary.models import Salary
from src.salary.schemas import SalarySchema


async def create_user(username: str, password: str, email: str, salary_id: int):
    hashed_password = get_password_hash(password)
    async for session in get_async_session():
        new_user = User(username=username, hashed_password=hashed_password, email=email, salary_id=salary_id)
        session.add(new_user)
        await session.commit()


async def create_salary(amount: float, next_raise_date: date) -> SalarySchema:
    async for session in get_async_session():
        new_salary = Salary(salary_amount=amount, next_raise_date=next_raise_date)
        session.add(new_salary)
        await session.commit()
        return SalarySchema.from_orm(new_salary)


if __name__ == '__main__':
    async def main():
        tasks = [create_salary(i * 1000, date(2027, 1, (i % 29)+1)) for i in range(10)]
        salaries = await asyncio.gather(*tasks)

        tasks = [create_user(f'user{i}', f'password{i}', f'email{i}', salary.id) for i, salary in enumerate(salaries)]
        await asyncio.gather(*tasks)

    asyncio.run(main())
