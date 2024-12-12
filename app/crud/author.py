from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.models.author import Author
from schemas import AuthorCreate, AuthorUpdate, AuthorUpdatePartial


async def get_all_authors(
    session: AsyncSession,
) -> Sequence[Author]:
    stmt = select(Author).order_by(Author.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_author(session: AsyncSession, author_id: int) -> Author | None:
    return await session.get(Author, author_id)


async def create_author(
    session: AsyncSession,
    author_create: AuthorCreate,
) -> Author:
    author = Author(**author_create.model_dump())
    session.add(author)
    await session.commit()
    await session.refresh(author)
    return author


async def update_author(
    session: AsyncSession,
    author: Author,
    author_update: AuthorUpdate | AuthorUpdatePartial,
    partial: bool = False,
) -> Author:
    for name, value in author_update.model_dump(exclude_unset=partial).items():
        setattr(author, name, value)
    await session.commit()
    return author


async def delete_author(
    session: AsyncSession,
    author: Author,
) -> None:
    await session.delete(author)
    await session.commit()