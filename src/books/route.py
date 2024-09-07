from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from typing import List
from src.books.book_data import Book_data
from src.books.schema import bookupdatemodel, Book


book_router = APIRouter()

@book_router.get("/books", response_model=list[Book])
async def get_allbook():
    return Book_data

@book_router.get("/book/{book_id}" )
async def get_a_book(book_id:int):
    for book_var in Book_data:
        if book_var["id"] == book_id:
            return book_var
    return {"book id does noexist"}

@book_router.post("/book", status_code=status.HTTP_201_CREATED)
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
        
        