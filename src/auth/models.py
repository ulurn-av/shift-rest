from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

from src.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    middle_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    salary_id: Mapped[int] = mapped_column(ForeignKey("salaries.id", ondelete="SET NULL"))


class Salary(Base):
    __tablename__ = "salaries"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[int]
    date: Mapped[date]
