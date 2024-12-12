from sqlalchemy.orm import Mapped, relationship
from .base import Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .book import Book


class Author(Base):
    name: Mapped[str]
    books: Mapped["Book"] = relationship(back_populates="author")
