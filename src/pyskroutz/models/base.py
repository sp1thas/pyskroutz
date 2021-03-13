from typing import List, Dict, Optional, Any

from pydantic import BaseModel, HttpUrl, PositiveInt


class PaginationItem(BaseModel):
    """Pagination model.

    Attributes:
        total_results:
        total_pages:
        page:
        per:
    """

    page: int
    per: int
    total_pages: int
    total_results: int


class AvailabilityItem(BaseModel):
    count: int
    id: int
    label: str


class DistaceItem(BaseModel):
    count: int
    id: int
    label: str


class AvailabilityFilterItem(BaseModel):
    availabilities: Optional[List[AvailabilityItem]]
    distances: Optional[List[AvailabilityItem]]
    filters: Optional[Dict[str, int]]
    manufacturers: Optional[Dict[str, int]]
    shops: Optional[Dict[str, int]]


class SkuRatingBreakDownItem(BaseModel):
    count: int
    percentage: int
    star: int


class SkuReviewsAggrItem(BaseModel):
    label: str
    score: int
    style: str


class LocationItem(BaseModel):
    address_id: Optional[int]
    country_code: str
    label: str
    lat: str
    lng: str
    type: str


class PaymentMethodTypeItem(BaseModel):
    type: Any


class PersonalizationItem(BaseModel):
    location: LocationItem
    payment_method: PaymentMethodTypeItem


class MetaItemBase(BaseModel):
    """Meta model.

    Attributes:
        pagination:
    """

    available_filters: Optional[AvailabilityFilterItem]
    order_by: Optional[str]
    order_by_methods: Optional[Dict[str, str]]
    pagination: Optional[PaginationItem]
    personalization: Optional[PersonalizationItem]
    sku_rating_breakdown: Optional[List[SkuRatingBreakDownItem]]
    sku_reviews_aggregation: Optional[List[SkuReviewsAggrItem]]


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
    name: Optional[str]


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

    price_max: Optional[float]
    price_min: Optional[float]
    reviewable: Optional[bool]
    reviews_count: Optional[int]
    reviewscore: Optional[float]
    shop_count: Optional[int]


class ImageItemBase(BaseModel):
    """Item image base model.

    Attributes:
        main:
        alternatives:
    """

    alternatives: Optional[List[HttpUrl]]
    main: Optional[HttpUrl]
