"""Response models for product resources
"""
from typing import List, Any, Optional

from pydantic import BaseModel, HttpUrl

from .base import WebUriBaseItem, ItemBase, MetaItemBase, PersonalizationItem
from .shops import ShopItem


class BlpItem(BaseModel):
    shipping_cost: float
    payment_method_cost: Optional[float]
    final_price: Optional[float]


class ProductItem(ItemBase, WebUriBaseItem):
    sku_id: int
    shop_id: int
    category_id: int
    availability: str
    click_url: HttpUrl
    shop_uid: str
    expenses: Optional[Any]
    sizes: List
    blp: Optional[BlpItem]
    price: float
    immediate_pickup: bool


class ProductRetrieve(BaseModel):
    product: Optional[ProductItem]
    meta: Optional[MetaItemBase]


class ProductsList(BaseModel):
    products: List[ProductItem]


class CardItem(BaseModel):
    products: Optional[List[ProductItem]]
    blp: Optional[BlpItem]
    shop: Optional[ShopItem]


class CardsList(BaseModel):
    product_cards: List[CardItem]
    meta: MetaItemBase


class PersonalizationRetrieve(BaseModel):
    personalization: PersonalizationItem
