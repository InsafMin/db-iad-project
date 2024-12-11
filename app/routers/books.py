from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.db_helper import db_helper
from crud import book as crud_book
from dependencies import book_by_id
from schemas import Book, BookUpdatePartial, BookUpdate, BookCreate

router = APIRouter()


@router.get("/", response_model=list[Book])
async def get_books(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    return await crud_book.get_all_books(session=session)


@router.post("/", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_book(
    book_create: BookCreate,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    return await crud_book.create_book(session=session, book_create=book_create)


@router.get("/{book_id}", response_model=Book)
async def get_book(
    book: Book = Depends(book_by_id),
):
    return book


@router.put("/{book_id}/")
async def update_book(
    book_update: BookUpdate,
    book: Book = Depends(book_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud_book.update_book(
        session=session,
        book=book,
        book_update=book_update,
    )


@router.patch("/{book_id}/")
async def update_book_partial(
    book_update: BookUpdatePartial,
    book: Book = Depends(book_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud_book.update_book(
        session=session,
        book=book,
        book_update=book_update,
        partial=True,
    )


@router.delete("/{book_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(
    book: Book = Depends(book_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
) -> None:
    await crud_book.delete_book(session=session, book=book)
