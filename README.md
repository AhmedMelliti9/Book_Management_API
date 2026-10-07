# Book Management API

A RESTful API for managing a collection of books, built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

The project demonstrates the fundamentals of backend API development, including CRUD operations, request validation, database integration, filtering, and structured interaction between a FastAPI application and a PostgreSQL database.

## Features

- Create a new book
- Retrieve all books
- Retrieve a book by ID
- Update an existing book
- Delete a book
- Search and filter books
- Filter by:
  - Title
  - Author
  - Category
  - Minimum pages
  - Maximum pages
  - Availability
- Request validation using Pydantic
- PostgreSQL database integration
- SQLAlchemy ORM for database operations
- HTTP error handling
- Interactive API documentation with Swagger UI

## Technologies

- **Python**
- **FastAPI** — Web framework for building the REST API
- **Pydantic** — Request and response validation
- **SQLAlchemy** — ORM for interacting with the database
- **PostgreSQL** — Relational database
- **Psycopg** — PostgreSQL database driver
- **Uvicorn** — ASGI server
- **Git & GitHub** — Version control

## Project Structure

```text
Book_Management_API/
│
├── main.py
├── models.py
├── schemas.py
├── db.py
├── database.py
├── requirements.txt
└── README.md
```

> The exact structure may vary depending on the current version of the project.

## How It Works

The application follows a simple backend architecture:

```text
Client
   │
   ▼
FastAPI
   │
   ▼
Pydantic Validation
   │
   ▼
SQLAlchemy ORM
   │
   ▼
PostgreSQL
```

FastAPI receives HTTP requests and validates the incoming data using Pydantic.

SQLAlchemy is responsible for communicating with PostgreSQL and performing database operations such as creating, reading, updating, and deleting books.

## Database

The project uses PostgreSQL to persist book data.

A typical `books` table contains information such as:

| Field | Description |
|---|---|
| `id` | Unique identifier |
| `title` | Book title |
| `author` | Book author |
| `pages` | Number of pages |
| `available` | Whether the book is available |
| `category` | Book category |

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/AhmedMelliti9/Book_Management_API.git
```

Navigate into the project:

```bash
cd Book_Management_API
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## PostgreSQL Configuration

Make sure PostgreSQL is installed and running.

Create a PostgreSQL database:

```sql
CREATE DATABASE book_management;
```

Configure your database connection according to your local PostgreSQL setup.

For example:

```text
postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/book_management
```

**Do not commit real database passwords or other credentials to GitHub.**

For a real project, these values should be stored in environment variables.

## Run the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to test the API endpoints directly from your browser.

### ReDoc

Alternative documentation is available at:

```text
http://127.0.0.1:8000/redoc
```

## API Endpoints

### Books

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/books` | Get all books |
| `GET` | `/books/{id}` | Get a book by ID |
| `POST` | `/books` | Create a new book |
| `PUT` | `/books/{id}` | Update a book |
| `DELETE` | `/books/{id}` | Delete a book |

### Filtering

The API supports filtering books based on different criteria.

Examples:

```text
GET /books?title=Python
```

```text
GET /books?author=George%20Orwell
```

```text
GET /books?category=Programming
```

```text
GET /books?min_pages=100&max_pages=500
```

```text
GET /books?available=true
```

Multiple filters can also be combined.

## Example Request

### Create a Book

```http
POST /books
```

Request body:

```json
{
  "id": 1,
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "pages": 464,
  "available": true,
  "category": "Programming"
}
```

Example response:

```json
{
  "id": 1,
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "pages": 464,
  "available": true,
  "category": "Programming"
}
```

## Error Handling

The API handles common errors using appropriate HTTP status codes.

- `200 OK` — Successful request
- `201 Created` — Resource successfully created
- `404 Not Found` — Requested book does not exist
- `400 Bad Request` — Invalid request
- `422 Unprocessable Entity` — Validation error

FastAPI and Pydantic provide automatic validation for request data.

## Learning Objectives

This project was developed to practice and understand:

- REST API development
- FastAPI fundamentals
- Pydantic data validation
- HTTP methods and status codes
- CRUD operations
- SQL fundamentals
- PostgreSQL
- SQLAlchemy ORM
- Database sessions
- Database models
- Querying and filtering
- Backend project structure
- API documentation

## Author

**Ahmed Melliti**

Computer Science Student interested in **Backend Software Engineering and AI Engineering**.

---

## License

This project is intended for educational and portfolio purposes.