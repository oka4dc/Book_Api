from fastapi import FastAPI
from src.books.route import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db


@asynccontextmanager
async def life_span(app:FastAPI):
    print("SERVER IS STARTING")
    await init_db()
    yield
    print("server has stopped")

version = "v1"

version_prefix =f"/api/{version}"

app = FastAPI(
    title="Bookly",
    description="description",
    version=version,
    license_info={"name": "MIT License", "url": "https://opensource.org/license/mit"},
    contact={
        "name": "Dennis Okafor",
        "url": "https://github.com/oka4dc",
        "email": "okaforchikelue93@gmail.com",
    },
    terms_of_service="httpS://example.com/tos",
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc",
    lifespan= life_span
)

app.include_router(book_router, prefix=f"{version_prefix}/books", tags=["books"])



