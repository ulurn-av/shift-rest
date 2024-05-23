from pydantic import BaseModel
from datetime import date


class SalaryOut(BaseModel):
    salary_amount: float
    next_raise_date: date

    class Config:
        orm_mode = True
