from sqlalchemy import Column, Integer, String, Boolean
from db import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    author = Column(String(100), nullable=False, index=True)
    pages = Column(Integer, nullable=False)
    available = Column(Boolean, nullable=False, default=True)
    category = Column(String(100), nullable=True, index=True)
