from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.db_helper import db_helper
from app import schemas
from app.crud import reader as crud_reader
from dependencies import reader_by_id
from schemas import Reader, ReaderUpdatePartial, ReaderUpdate

router = APIRouter()


@router.get("/", response_model=list[Reader])
async def get_reader(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    return await crud_reader.get_all_readers(session=session)


@router.post("/", response_model=Reader, status_code=status.HTTP_201_CREATED)
async def create_reader(
    reader_create: schemas.ReaderCreate,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    return await crud_reader.create_reader(session=session, reader_create=reader_create)


@router.get("/{reader_id}/", response_model=Reader)
async def get_reader(
    reader: Reader = Depends(reader_by_id),
):
    return reader


@router.put("/{reader_id}/")
async def update_reader(
    reader_update: ReaderUpdate,
    reader: Reader = Depends(reader_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud_reader.update_reader(
        session=session,
        reader=reader,
        reader_update=reader_update,
    )


@router.patch("/{reader_id}/")
async def update_reader_partial(
    reader_update: ReaderUpdatePartial,
    reader: Reader = Depends(reader_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud_reader.update_reader(
        session=session,
        reader=reader,
        reader_update=reader_update,
        partial=True,
    )


@router.delete("/{reader_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_reader(
    reader: Reader = Depends(reader_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
) -> None:
    await crud_reader.delete_reader(session=session, reader=reader)
