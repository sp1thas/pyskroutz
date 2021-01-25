from typing import List, Optional

from pydantic import BaseModel, HttpUrl


class PaginationResponseModel(BaseModel):
    """Pagination model.

    Attributes:
        total_results:
        total_pages:
        page:
        per:
    """

    total_results: int
    total_pages: int
    page: int
    per: int


class MetaResponseModel(BaseModel):
    """Meta model.

    Attributes:
        pagination:
    """

    pagination: PaginationResponseModel


class WebUriResponseModel(BaseModel):
    """Web URI model.

    Attributes:
        web_uri:
    """

    web_uri: HttpUrl


class ItemBaseResponseModel(BaseModel):
    """Item Base model.

    Attributes:
        id:
        name:
    """

    id: int
    name: str


class ItemBuyBaseResponseModel(BaseModel):
    """Item Buy base model.

    Attributes:
        price_min:
        price_max:
        shop_count:
        reviewscore:
        reviews_count:
        reviewable:
    """

    price_min: float
    price_max: float
    shop_count: int
    reviewscore: float
    reviews_count: int
    reviewable: Optional[bool]


class ItemImageBaseResponseModel(BaseModel):
    """Item image base model.

    Attributes:
        main:
        alternatives:
    """

    main: str
    alternatives: List[str]


class BookResponseModel(
    ItemBaseResponseModel, ItemBuyBaseResponseModel, WebUriResponseModel
):
    """Book response model.

    Attributes:
        main_author_id:
        main_author:
        images:
    """

    main_author_id: int
    main_author: str
    images: List[ItemImageBaseResponseModel]
