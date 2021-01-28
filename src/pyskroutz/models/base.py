from typing import List, Optional, Dict

from pydantic import BaseModel, HttpUrl, PositiveInt


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


class AvailabilityItem(BaseModel):
    id: int
    label: str
    count: int


class DistaceItem(BaseModel):
    id: int
    label: str
    count: int


class AvailabilityFilterItem(BaseModel):
    filters: Optional[Dict[str, int]]
    manufacturers: Optional[Dict[str, int]]
    shops: Optional[Dict[str, int]]
    availabilities: Optional[List[AvailabilityItem]]
    distances: Optional[List[AvailabilityItem]]


class SkuRatingBreakDownItem(BaseModel):
    star: int
    percentage: int
    count: int


class SkuReviewsAggrItem(BaseModel):
    label: str
    score: int
    style: str


class MetaItemBase(BaseModel):
    """Meta model.

    Attributes:
        pagination:
    """

    pagination: PaginationResponseModel
    order_by: Optional[str]
    order_by_methods: Optional[Dict[str, str]]
    available_filters: Optional[AvailabilityFilterItem]
    sku_reviews_aggregation: Optional[List[SkuReviewsAggrItem]]
    sku_rating_breakdown: Optional[List[SkuRatingBreakDownItem]]


class WebUriBaseItem(BaseModel):
    """Web URI model.

    Attributes:
        web_uri:
    """

    web_uri: Optional[HttpUrl]


class ItemBase(BaseModel):
    """Item Base model.

    Attributes:
        id:
        name:
    """

    id: PositiveInt
    name: str


class BuyableItemBase(BaseModel):
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


class ImageItemBase(BaseModel):
    """Item image base model.

    Attributes:
        main:
        alternatives:
    """

    main: Optional[HttpUrl]
    alternatives: Optional[List[HttpUrl]]
