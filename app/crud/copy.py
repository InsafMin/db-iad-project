from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.models.copy import Copy
from schemas import CopyUpdate, CopyUpdatePartial, CopyCreate


async def get_all_copies(
    session: AsyncSession,
) -> Sequence[Copy]:
    stmt = select(Copy).order_by(Copy.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_copy(session: AsyncSession, copy_id: int) -> Copy | None:
    return await session.get(Copy, copy_id)


async def create_copy(
    session: AsyncSession,
    copy_create: CopyCreate,
) -> Copy:
    copy = Copy(**copy_create.model_dump())
    session.add(copy)
    await session.commit()
    await session.refresh(copy)
    return copy


async def update_copy(
    session: AsyncSession,
    copy: Copy,
    copy_update: CopyUpdate | CopyUpdatePartial,
    partial: bool = False,
) -> Copy:
    for name, value in copy_update.model_dump(exclude_unset=partial).items():
        setattr(copy, name, value)
    await session.commit()
    return copy


async def delete_copy(
    session: AsyncSession,
    copy: Copy,
) -> None:
    await session.delete(copy)
    await session.commit()