from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.models.book import Book
from schemas import BookCreate, BookUpdate, BookUpdatePartial


async def get_all_books(
    session: AsyncSession,
) -> Sequence[Book]:
    stmt = select(Book).order_by(Book.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_book(session: AsyncSession, book_id: int) -> Book | None:
    return await session.get(Book, book_id)


async def create_book(
    session: AsyncSession,
    book_create: BookCreate,
) -> Book:
    if book_create.published_year:
        bool.return_date = book_create.published_year.replace(tzinfo=None)
    book = Book(**book_create.model_dump())
    session.add(book)
    await session.commit()
    await session.refresh(book)
    return book


async def update_book(
    session: AsyncSession,
    book: Book,
    book_update: BookUpdate | BookUpdatePartial,
    partial: bool = False,
) -> Book:
    for name, value in book_update.model_dump(exclude_unset=partial).items():
        setattr(book, name, value)
    await session.commit()
    return book


async def delete_book(
    session: AsyncSession,
    book: Book,
) -> None:
    await session.delete(book)
    await session.commit()