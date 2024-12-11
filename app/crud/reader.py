from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.models.reader import Reader
from schemas import ReaderCreate, ReaderUpdate, ReaderUpdatePartial


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


async def update_reader(
    session: AsyncSession,
    reader: Reader,
    reader_update: ReaderUpdate | ReaderUpdatePartial,
    partial: bool = False,
) -> Reader:
    for name, value in reader_update.model_dump(exclude_unset=partial).items():
        setattr(reader, name, value)
    await session.commit()
    return reader


async def delete_reader(
    session: AsyncSession,
    reader: Reader,
) -> None:
    await session.delete(reader)
    await session.commit()