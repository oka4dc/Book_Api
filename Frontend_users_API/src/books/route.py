from typing import List

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from src.auth.dependencies import AccessTokenBearer, RoleChecker
from src.books.service import BookService
from src.db.main import get_session

from .schemas import Book, BookCreateModel, BookDetailModel, BookUpdateModel
from src.errors import BookNotFound

book_router = APIRouter()
book_service = BookService()
acccess_token_bearer = AccessTokenBearer()
role_checker = Depends(RoleChecker(["admin", "user"]))


@book_router.get("/", response_model=List[Book], dependencies=[role_checker])
async def get_all_books(
    session: AsyncSession = Depends(get_session),
    _: dict = Depends(acccess_token_bearer),
):
    books = await book_service.get_all_books(session)
    return books


@book_router.get(
    "/user/{user_uid}", response_model=List[Book], dependencies=[role_checker]
)
async def get_user_book_submissions(
    user_uid: str,
    session: AsyncSession = Depends(get_session),
    _: dict = Depends(acccess_token_bearer),
):
    books = await book_service.get_user_books(user_uid, session)
    return books


@book_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=Book,
    dependencies=[role_checker],
)
async def create_a_book(
    book_data: BookCreateModel,
    session: AsyncSession = Depends(get_session),
    token_details: dict = Depends(acccess_token_bearer),
) -> dict:
    user_id = token_details.get("user")["user_uid"]
    new_book = await book_service.create_book(book_data, user_id, session)
    return new_book


@book_router.get(
    "/{book_uid}", response_model=BookDetailModel, dependencies=[role_checker]
)
async def get_book(
    book_uid: str,
    session: AsyncSession = Depends(get_session),
    _: dict = Depends(acccess_token_bearer),
) -> dict:
    book = await book_service.get_book(book_uid, session)

    if book:
        return book
    else:
        raise BookNotFound()


@book_router.patch("/{book_uid}", response_model=Book, dependencies=[role_checker])
async def update_book(
    book_uid: str,
    book_update_data: BookUpdateModel,
    session: AsyncSession = Depends(get_session),
    _: dict = Depends(acccess_token_bearer),
) -> dict:
    updated_book = await book_service.update_book(book_uid, book_update_data, session)

    if updated_book is None:
        raise BookNotFound()
    else:
        return updated_book


@book_router.delete(
    "/{book_uid}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[role_checker]
)
async def delete_book(
    book_uid: str,
    session: AsyncSession = Depends(get_session),
    _: dict = Depends(acccess_token_bearer),
):
    book_to_delete = await book_service.delete_book(book_uid, session)

    if book_to_delete is None:
        raise BookNotFound()
    else:
        return {}

"""
from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from typing import List
from src.books.book_data import Book_data
from src.books.schema import bookupdatemodel, Book

book_router = APIRouter()

@book_router.get("/books", response_model=list[Book])
async def get_allbook()->dict:
    return Book_data

@book_router.get("/book/{book_id}" )
async def get_a_book(book_id:int)->dict:
    for book_var in Book_data:
        if book_var["id"] == book_id:
            return book_var
    return {"book id does noexist"}

@book_router.post("/books", status_code=status.HTTP_201_CREATED)
async def create_book(book_data: Book)->dict:
    new_book =book_data.model_dump()
    book_data.append(new_book)
    return new_book

@book_router.patch("/books/{book_id}" )
async def update_book(book_id:int, book_update_data:bookupdatemodel):
    for book_var in Book_data:
        if book_var["id"] == book_id:
            book_var["title"] = book_update_data.title
            book_var["publisher"] = book_update_data.publisher
            book_var["page_count"] = book_update_data.page_count
            book_var["language"] = book_update_data.language
            
            return book_var
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="book not found")


@book_router.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int, book_update_data:Book):
    for book_var in Book_data:
        if book_var["id"] == book_id:
            Book_data.remove(book_var)
            
            return {} 
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="book not found")      
        
"""