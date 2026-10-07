import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/book_management"
)

connect_args = (
    {"check_same_thread": False}
    if DATABASE_URL.startswith("sqlite")
    else {}
)

engine = create_engine(DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base = declarative_base()


def init_db():
    from models import Book  # noqa: F401

    try:
        Base.metadata.create_all(bind=engine)
    except Exception as exc:
        print(f"Database initialization warning: {exc}")


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
