from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Reader, Book, Copy, Borrowing
from schemas import ReaderCreate


async def get_all_readers(
    session: AsyncSession,
) -> Sequence[Reader]:
    stmt = select(Reader).order_by(Reader.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_reader(session: AsyncSession, reader_id: int) -> Reader | None:
    return await session.get(Reader, reader_id)


async def create_reader(
    session: AsyncSession,
    reader_create: ReaderCreate,
) -> Reader:
    reader = Reader(**reader_create.model_dump())
    session.add(reader)
    await session.commit()
    await session.refresh(reader)
    return reader
