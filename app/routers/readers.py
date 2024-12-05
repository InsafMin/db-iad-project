from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import db_helper
from app import crud, schemas
from schemas import Reader

router = APIRouter()


@router.get("/", response_model=list[Reader])
async def get_reader(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    return await crud.get_all_readers(session=session)


@router.post("/", response_model=Reader)
async def create_reader(
    reader_create: schemas.ReaderCreate,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    return await crud.create_reader(session=session, reader_create=reader_create)


@router.get("/{reader_id}", response_model=Reader)
async def get_reader(
    reader_id: int,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    db_reader = await crud.get_reader(session, reader_id)
    if not db_reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    return db_reader
