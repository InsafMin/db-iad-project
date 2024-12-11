from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from core.models.db_helper import db_helper
from routers import readers, books, borrowings, copies
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
        # await conn.run_sync(Base.metadata.drop_all)
    yield
    await db_helper.dispose()


main_app = FastAPI(lifespan=lifespan)
main_app.include_router(readers.router, prefix="/readers", tags=["Readers"])
main_app.include_router(books.router, prefix="/books", tags=["Books"])
main_app.include_router(copies.router, prefix="/copies", tags=["Copies"])
main_app.include_router(borrowings.router, prefix="/borrowing", tags=["Borrowings"])


@main_app.get("/")
def welcome():
    return {
        "message": "Welcome to Library!",
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
