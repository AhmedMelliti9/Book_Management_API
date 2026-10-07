from pydantic import BaseModel, ConfigDict


class BookBase(BaseModel):
    title: str
    author: str
    pages: int
    available: bool = True
    category: str | None = None


class BookCreate(BookBase):
    id: int | None = None


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    pages: int | None = None
    available: bool | None = None
    category: str | None = None


class BookResponse(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)