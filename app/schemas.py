from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional, Annotated
from datetime import datetime


class ReaderBase(BaseModel):
    first_name: Annotated[str, MinLen(2), MaxLen(20)]
    last_name: Annotated[str, MinLen(2), MaxLen(40)]
    email: EmailStr
    is_active: bool = True


class ReaderCreate(ReaderBase):
    pass


class Reader(ReaderBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


# class BookBase(BaseModel):
#     ISBN: int
#     title: str
#     author: str
#     published_year: datetime
#     category: str
#
#
# class BookCreate(BookBase):
#     pass
#
#
# class BookOut(BookBase):
#     model_config = ConfigDict(from_attributes=True)
#
#
# class CopyBase(BaseModel):
#     id: int
#     ISBN: int
#
#
# class CopyCreate(CopyBase):
#     pass
#
#
# class CopyOut(CopyBase):
#     model_config = ConfigDict(from_attributes=True)
#
#
# class BorrowingBase(BaseModel):
#     copy_id: int
#     reader_id: int
#     borrow_date: datetime
#     return_date: Optional[datetime]
#
#
# class BorrowingCreate(BorrowingBase):
#     pass
#
#
# class BorrowingOut(BorrowingBase):
#     model_config = ConfigDict(from_attributes=True)
