from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from db import get_db, init_db
from models import Book
from schemas import BookCreate, BookResponse, BookUpdate


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Book Management API",
    description="A RESTful API for managing a collection of books",
    version="1.0.0",
    lifespan=lifespan,
)


# Root route
@app.get("/")
def root():
    return {
        "message": "Welcome to the Book Management API",
        "docs_url": "/docs",
        "redoc_url": "/redoc",
    }


# Get all books with optional filtering
@app.get("/books", response_model=list[BookResponse])
def get_books(
    title: str | None = None,
    author: str | None = None,
    category: str | None = None,
    min_pages: int | None = None,
    max_pages: int | None = None,
    available: bool | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(Book)

    if title is not None:
        query = query.filter(Book.title.ilike(f"%{title}%"))

    if author is not None:
        query = query.filter(Book.author.ilike(f"%{author}%"))

    if category is not None:
        query = query.filter(Book.category.ilike(f"%{category}%"))

    if min_pages is not None:
        query = query.filter(Book.pages >= min_pages)

    if max_pages is not None:
        query = query.filter(Book.pages <= max_pages)

    if available is not None:
        query = query.filter(Book.available == available)

    return query.all()


# Create a book
@app.post("/books", response_model=BookResponse, status_code=201)
def create_book(
    book: BookCreate,
    db: Session = Depends(get_db),
):
    if book.id is not None:
        existing_book = db.query(Book).filter(Book.id == book.id).first()

        if existing_book:
            raise HTTPException(
                status_code=400,
                detail="Book with this ID already exists",
            )

        new_book = Book(
            id=book.id,
            title=book.title,
            author=book.author,
            pages=book.pages,
            available=book.available,
            category=book.category,
        )
    else:
        new_book = Book(
            title=book.title,
            author=book.author,
            pages=book.pages,
            available=book.available,
            category=book.category,
        )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


# Get available books
@app.get("/books/available", response_model=list[BookResponse])
def available_books(
    db: Session = Depends(get_db),
):
    books = db.query(Book).filter(Book.available == True).all()  # noqa: E712

    return books


# Get books by author
@app.get("/books/author/{author}", response_model=list[BookResponse])
def author_books(
    author: str,
    db: Session = Depends(get_db),
):
    books = db.query(Book).filter(Book.author.ilike(f"%{author}%")).all()

    return books


# Count books
@app.get("/books/count")
def count_books(
    db: Session = Depends(get_db),
):
    count = db.query(Book).count()

    return {"count": count}


# Search books by title
@app.get("/books/search", response_model=list[BookResponse])
def title_books(
    title: str,
    db: Session = Depends(get_db),
):
    books = db.query(Book).filter(Book.title.ilike(f"%{title}%")).all()

    return books


# Filter books by number of pages
@app.get("/books/filter", response_model=list[BookResponse])
def filter_books(
    min_pages: int | None = None,
    max_pages: int | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(Book)

    if min_pages is not None:
        query = query.filter(Book.pages >= min_pages)

    if max_pages is not None:
        query = query.filter(Book.pages <= max_pages)

    books = query.all()

    return books


# Get a book by ID (must be declared after the static /books/* routes)
@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(
    book_id: int,
    db: Session = Depends(get_db),
):
    book = db.query(Book).filter(Book.id == book_id).first()

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found",
        )

    return book


# Update a book
@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    book: BookUpdate,
    db: Session = Depends(get_db),
):
    existing_book = db.query(Book).filter(Book.id == book_id).first()

    if existing_book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found",
        )

    update_data = book.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(existing_book, field, value)

    db.commit()
    db.refresh(existing_book)

    return existing_book


# Delete a book
@app.delete("/books/{book_id}")
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
):
    book = db.query(Book).filter(Book.id == book_id).first()

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found",
        )

    db.delete(book)
    db.commit()

    return {"message": "Book deleted successfully"}
