from fastapi import FastAPI

app = FastAPI()



Book = [
    {
        "id":1,
        "title":"Think python",
        "author":"dan wood",
        "publisher":"O Relly",
        "page_count":750,
        "language":"English"
    }, 
    {
        "id":2,
        "title":"python intro",
        "author":"walter watr",
        "publisher":"bush pub",
        "page_count":2750,
        "language":"English"
    },
    {
        "id":3,
        "title":"Engineering athematics",
        "author":"hez fourier",
        "publisher":"landmark",
        "page_count":5450,
        "language":"igbo"
    },
    {
        "id":4,
        "title":"Think python",
        "author":"dan wood",
        "publisher":"O Relly",
        "page_count":50,
        "language":"spanish"
    }
    
    
    
]

@app.get("/books", )
async def get_allbook():
    return Book

@app.get("/books/{id}" )
async def get_book(id:int):
    for book in Book:
        if book["id"] == [id]:
            return book
        else:    
            return {"book id does noexist"}

@app.post("/books", )
async def book():
    return Book[0]
@app.put("/book", )
async def book():
    return Book[1]
@app.delete("/book", )
async def book():
    return Book