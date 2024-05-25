from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, index=True)
    name: Mapped[str | None]
    middle_name: Mapped[str | None]
    last_name: Mapped[str | None]
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    salary_id: Mapped[int | None] = mapped_column(ForeignKey("salaries.id", ondelete="SET NULL"), index=True)
