from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.models.borrowing import Borrowing
from schemas import BorrowingCreate, BorrowingUpdate, BorrowingUpdatePartial


async def get_all_borrowings(
    session: AsyncSession,
) -> Sequence[Borrowing]:
    stmt = select(Borrowing).order_by(Borrowing.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_borrowing(session: AsyncSession, borrowing_id: int) -> Borrowing | None:
    return await session.get(Borrowing, borrowing_id)


async def create_borrowing(
    session: AsyncSession,
    borrowing_create: BorrowingCreate,
) -> Borrowing:
    borrowing_create.borrow_date = borrowing_create.borrow_date.replace(tzinfo=None)
    if borrowing_create.return_date:
        borrowing_create.return_date = borrowing_create.return_date.replace(tzinfo=None)
    borrowing = Borrowing(**borrowing_create.model_dump())
    session.add(borrowing)
    await session.commit()
    await session.refresh(borrowing)
    return borrowing


async def update_borrowing(
    session: AsyncSession,
    borrowing: Borrowing,
    borrowing_update: BorrowingUpdate | BorrowingUpdatePartial,
    partial: bool = False,
) -> Borrowing:
    if borrowing_update.borrow_date:
        borrowing_update.borrow_date = borrowing_update.borrow_date.replace(tzinfo=None)
    if borrowing_update.return_date:
        borrowing_update.return_date = borrowing_update.return_date.replace(tzinfo=None)
    for name, value in borrowing_update.model_dump(exclude_unset=partial).items():
        setattr(borrowing, name, value)
    await session.commit()
    return borrowing


async def delete_borrowing(
    session: AsyncSession,
    borrowing: Borrowing,
) -> None:
    await session.delete(borrowing)
    await session.commit()