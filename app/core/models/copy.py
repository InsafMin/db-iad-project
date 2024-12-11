from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from .book import Book
    from .borrowing import Borrowing
    from .reader import Reader


class Copy(Base):
    __tablename__ = "copies"

    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    book: Mapped["Book"] = relationship(back_populates="copies")

    # many-to-many relationship to Reader, bypassing the `Borrowing` class
    readers: Mapped[List["Reader"]] = relationship(
        secondary="borrowings", back_populates="copies"
    )

    # association between Copy -> Borrowing -> Reader
    reader_borrowing: Mapped[List["Borrowing"]] = relationship(back_populates="copy", overlaps="readers")
