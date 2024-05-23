from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date


class Salary(Base):
    __tablename__ = "salaries"

    id: Mapped[int] = mapped_column(primary_key=True)
    salary_amount: Mapped[int]
    next_raise_date: Mapped[date]