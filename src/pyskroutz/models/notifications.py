"""Response models for notifications resources
"""
import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, HttpUrl

from .base import MetaItemBase
from .skus import SkuItem


class NotificationType(Enum):
    PRICE_DROP = "price_drop"
    AVAILABILITY_TRUE = "availability_true"
    SKU_RELEASE = "sku_release"
    SKU_REVIEW = "sku_review"
    SKU_REVIEW_REPHRASE_REQUEST = "sku_review_rephrase_request"
    SKU_REVIEW_APPROVE_AFTER_UPDATE = "sku_review_approve_after_update"


class SnapshotItem(BaseModel):
    price_min: float
    latest_price: float
    change_rate: float
    from_threshold: bool


class NotificationItem(BaseModel):
    id: int
    etype: NotificationType
    eventable_id: int
    eventable_type: str
    eventable_name: str
    eventable_url: HttpUrl
    event_text: Optional[str]
    is_viewed: bool
    aggregated: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    sku: Optional[SkuItem]
    category_name: str


class NotificationList(BaseModel):
    notifications: Optional[List[NotificationItem]]
    meta: MetaItemBase


class NotificationRetrieve(BaseModel):
    notification: NotificationItem
