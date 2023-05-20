"""Response models for book resources
"""

from typing import Any, List, Optional

from pydantic import BaseModel, EmailStr, HttpUrl, PositiveInt

from pyskroutz.models.base import (
    BuyableItemBase,
    ImageItemBase,
    ItemBase,
    MetaItemBase,
    WebUriBaseItem,
)


class BookItem(ItemBase, BuyableItemBase, WebUriBaseItem):
    """Book response model.

    Attributes:
        main_author_id:
        main_author:
        images:
    """

    main_author_id: Optional[PositiveInt]
    main_author: Optional[str]
    images: Optional[ImageItemBase]


class BooksRetrieve(BaseModel):
    """

    Attributes:
        book: Book item.
    """

    book: BookItem


class BookAuthorItem(BaseModel):
    id: PositiveInt
    name: str
    bio: str
    image: HttpUrl


class BookDetailsItem(BaseModel):
    series: str
    cover: str
    pubyear: str
    pages: int
    isbn: str
    shape: str
    volume: Optional[Any]
    ages: Optional[Any]
    description: str


class BookDetailsRetrieve(BaseModel):
    book_details: BookDetailsItem


class BookAuthorRetrieve(BaseModel):
    author: BookAuthorItem


class BooksList(BaseModel):
    books: Optional[List[BookItem]]
    meta: Optional[MetaItemBase]


class PublisherItem(ItemBase):
    id: PositiveInt
    name: str
    address: str
    email: EmailStr
    website: str
    fax: str
    phone: str


class PublisherRetrieve(BaseModel):
    publisher: PublisherItem


class BookCategory(BaseModel):
    id: PositiveInt
    name: str
    match_count: Optional[int]


class BookCategoryRetrieve(BaseModel):
    category: Optional[BookCategory]


class BookCategoriesList(BaseModel):
    categories: List[BookCategory]
