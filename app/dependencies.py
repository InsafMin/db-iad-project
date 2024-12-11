from typing import Annotated
from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession
from crud import book as crud_book, reader as crud_reader, borrowing as crud_borrowing, copy as crud_copy
from core.models import db_helper


async def reader_by_id(
    reader_id: Annotated[int, Path],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    reader = await crud_reader.get_reader(session, reader_id)
    if reader:
        return reader

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Reader {reader_id} not found")


async def book_by_id(
    book_id: Annotated[int, Path],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    book = await crud_book.get_book(session, book_id)
    if book:
        return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book {book_id} not found")


async def copy_by_id(
    copy_id: Annotated[int, Path],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    copy = await crud_copy.get_copy(session, copy_id)
    if copy:
        return copy

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Copy {copy_id} not found")


async def borrowing_by_id(
    borrowing_id: Annotated[int, Path],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    borrowing = await crud_borrowing.get_borrowing(session, borrowing_id)
    if borrowing:
        return borrowing

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Borrowing {borrowing_id} not found")