from pydantic import BaseModel
from datetime import date


class SalaryOut(BaseModel):
    salary_amount: float
    next_raise_date: date

    class Config:
        from_attributes = True


class SalarySchema(SalaryOut):
    id: int

    class Config:
        from_attributes = True
