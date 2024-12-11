from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from .base import Base
if TYPE_CHECKING:
    from .copy import Copy
    from .reader import Reader


class Borrowing(Base):
    id = None
    reader_id: Mapped[int] = mapped_column(ForeignKey("readers.id"), primary_key=True)
    copy_id: Mapped[int] = mapped_column(ForeignKey("copies.id"), primary_key=True)
    borrow_date: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now,
        primary_key=True,
    )
    return_date: Mapped[datetime | None] = mapped_column(
        server_default=func.now(),
        default=None,
    )

    # association between Borrowing -> Book
    copy: Mapped["Copy"] = relationship(back_populates="reader_borrowing", overlaps="readers")

    # association between Borrowing -> Reader
    reader: Mapped["Reader"] = relationship(back_populates="copy_borrowing", overlaps="readers")