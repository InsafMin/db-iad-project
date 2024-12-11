from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, relationship, mapped_column
from .base import Base
if TYPE_CHECKING:
    from .borrowing import Borrowing
    from .copy import Copy


class Reader(Base):
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)

    copies: Mapped[List["Copy"]] = relationship(
        secondary="borrowings", back_populates="readers", overlaps="copy, reader_borrowing, reader"
    )

    # association between Reader -> Borrowing -> Copy
    copy_borrowing: Mapped[List["Borrowing"]] = relationship(back_populates="reader", overlaps="copies,readers")
