from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.db_helper import db_helper
from crud import author as crud_author
from dependencies import author_by_id
from schemas import Author, AuthorUpdatePartial, AuthorUpdate, AuthorCreate

router = APIRouter()


@router.get("/", response_model=list[Author])
async def get_authors(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    return await crud_author.get_all_authors(session=session)


@router.post("/", response_model=Author, status_code=status.HTTP_201_CREATED)
async def create_author(
    author_create: AuthorCreate,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    return await crud_author.create_author(session=session, author_create=author_create)


@router.get("/{author_id}", response_model=Author)
async def get_author(
    author: Author = Depends(author_by_id),
):
    return author


@router.put("/{author_id}/")
async def update_author(
    author_update: AuthorUpdate,
    author: Author = Depends(author_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud_author.update_author(
        session=session,
        author=author,
        author_update=author_update,
    )


@router.patch("/{author_id}/")
async def update_author_partial(
    author_update: AuthorUpdatePartial,
    author: Author = Depends(author_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud_author.update_author(
        session=session,
        author=author,
        author_update=author_update,
        partial=True,
    )


@router.delete("/{author_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_author(
    author: Author = Depends(author_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
) -> None:
    await crud_author.delete_author(session=session, author=author)
