"""Response models for shop resources
"""
from typing import List, Optional

from pydantic import BaseModel, HttpUrl

from .base import ItemBase, WebUriBaseItem, MetaItemBase
from .users import AddressItem


class PaymentMethodsItem(BaseModel):
    credit_card: bool
    paypal: bool
    bank: bool
    spot_cash: bool
    installments: Optional[str]


class ShippingItem(BaseModel):
    free: bool
    free_from: int
    free_from_info: str
    min_price: str
    shipping_cost_enabled: bool


class ExtraInfoItem(BaseModel):
    time_on_platform: str
    orders_per_week: str


class ShopItem(ItemBase, WebUriBaseItem):
    link: HttpUrl
    phone: str
    image_url: HttpUrl
    thumbshot_url: HttpUrl
    reviews_count: int
    latest_reviews_count: int
    review_score: float
    payment_methods: PaymentMethodsItem
    shipping: ShippingItem
    extra_info: ExtraInfoItem
    top_positive_reasons: List[str]


class ShopRetrieve(BaseModel):
    shop: ShopItem


class ShopList(BaseModel):
    shops: Optional[List[ShopItem]]
    meta: MetaItemBase


class LocationItem(BaseModel):
    id: int
    headquarter: bool
    phones: Optional[List[str]]
    pickup_point: bool
    store: bool
    full_address: str
    format: str
    lat: Optional[str]
    lng: Optional[str]
    info: str
    address: Optional[AddressItem]


class LocationList(BaseModel):
    locations: List[LocationItem]
    meta: MetaItemBase


class LocationRetrieve(BaseModel):
    location: LocationItem
