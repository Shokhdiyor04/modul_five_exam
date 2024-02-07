import datetime
from typing import List

from sqlalchemy import BIGINT, TIMESTAMP, func, ForeignKey, FLOAT, CheckConstraint, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    chat_id: Mapped[int] = mapped_column(unique=True)
    fullname: Mapped[str] = mapped_column(__type_pos=VARCHAR)
    joined_at: datetime.datetime = mapped_column(TIMESTAMP, default=func.current_timestamp)


Base.metadata.crete_all(engine)