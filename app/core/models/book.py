from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from datetime import datetime
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from .author import Author
    from .copy import Copy


class Book(Base):
    title: Mapped[str]
    category: Mapped[str]
    published_year: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now,
    )
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship(back_populates="books")
    copies: Mapped[List["Copy"]] = relationship(back_populates="book")
