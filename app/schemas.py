from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Annotated
from datetime import datetime


class ReaderBase(BaseModel):
    first_name: Annotated[str, MinLen(2), MaxLen(20)]
    last_name: Annotated[str, MinLen(2), MaxLen(40)]
    email: EmailStr


class ReaderCreate(ReaderBase):
    pass


class Reader(ReaderBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class ReaderUpdate(ReaderCreate):
    pass


class ReaderUpdatePartial(ReaderCreate):
    first_name: Annotated[str, MinLen(2), MaxLen(20)] | None = None
    last_name: Annotated[str, MinLen(2), MaxLen(40)] | None = None
    email: EmailStr | None = None


class BookBase(BaseModel):
    title: Annotated[str, MinLen(2), MaxLen(100)]
    author: Annotated[str, MinLen(2), MaxLen(50)]
    published_year: datetime | None = None
    category: Annotated[str, MinLen(2), MaxLen(50)]


class BookCreate(BookBase):
    pass


class Book(BookBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class BookUpdate(BookCreate):
    pass


class BookUpdatePartial(BookCreate):
    title: Annotated[str, MinLen(2), MaxLen(100)] | None = None
    author: Annotated[str, MinLen(2), MaxLen(50)] | None = None
    category: Annotated[str, MinLen(2), MaxLen(50)] | None = None


class CopyBase(BaseModel):
    book_id: int


class CopyCreate(CopyBase):
    pass


class Copy(CopyBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class CopyUpdate(CopyCreate):
    pass


class CopyUpdatePartial(CopyCreate):
    book_id: int


class BorrowingBase(BaseModel):
    copy_id: int
    reader_id: int
    borrow_date: datetime
    return_date: datetime | None = None


class BorrowingCreate(BorrowingBase):
    pass


class Borrowing(BorrowingBase):
    model_config = ConfigDict(from_attributes=True)


class BorrowingUpdate(BorrowingCreate):
    pass


class BorrowingUpdatePartial(BorrowingCreate):
    copy_id: int | None = None
    reader_id: int | None = None
    borrow_date: datetime | None = None
