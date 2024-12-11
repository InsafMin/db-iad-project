from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.db_helper import db_helper
from crud import copy as crud_copy
from dependencies import copy_by_id
from schemas import Copy, CopyUpdatePartial, CopyUpdate, CopyCreate

router = APIRouter()


@router.get("/", response_model=list[Copy])
async def get_copies(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    return await crud_copy.get_all_copies(session=session)


@router.post("/", response_model=Copy, status_code=status.HTTP_201_CREATED)
async def create_copy(
    copy_create: CopyCreate,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    return await crud_copy.create_copy(
        session=session, copy_create=copy_create
    )


@router.get("/{copy_id}/", response_model=Copy)
async def get_copy(
    copy: Copy = Depends(copy_by_id),
):
    return copy


@router.put("/{copy_id}/")
async def update_copy(
    copy_update: CopyUpdate,
    copy: Copy = Depends(copy_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud_copy.update_copy(
        session=session,
        copy=copy,
        copy_update=copy_update,
    )


@router.patch("/{copy_id}/")
async def update_copy_partial(
    copy_update: CopyUpdatePartial,
    copy: Copy = Depends(copy_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud_copy.update_copy(
        session=session,
        copy=copy,
        copy_update=copy_update,
        partial=True,
    )


@router.delete("/{copy_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_reader(
    copy: Copy = Depends(copy_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
) -> None:
    await crud_copy.delete_copy(session=session, copy=copy)
