from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from datetime import datetime
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from .copy import Copy


class Book(Base):
    title: Mapped[str]
    author: Mapped[str]
    category: Mapped[str]
    published_year: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now,
    )

    copies: Mapped[List["Copy"]] = relationship(back_populates="book")
