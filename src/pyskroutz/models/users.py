"""Response models for User resources
"""
import datetime
from enum import Enum

from pydantic import AnyHttpUrl, EmailStr

from .base import *


class SexEnum(Enum):
    male = "male"
    female = "female"


class StatsItem(BaseModel):
    sku_review_count: int
    shop_review_count: int
    sku_comment_count: int
    received_votes: int


class EmailNotificationItem(BaseModel):
    field: str
    label: str
    description: str
    enabled: bool


class UserItem(BaseModel):
    id: int
    username: str
    avatar: AnyHttpUrl
    sex: SexEnum
    created_at: datetime.datetime
    email: EmailStr
    birthyear: Optional[int]
    mobile: Optional[str]
    type: str
    stats: StatsItem
    email_notifications: List[EmailNotificationItem]


class UserRetrieve(BaseModel):
    user: Optional[UserItem]


class AvatarList(BaseModel):
    avatars: List[AnyHttpUrl]


class AddressItem(BaseModel):
    id: int
    label: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    street_name: Optional[str]
    street_number: int
    city: str
    zip: Optional[str]
    region: str
    phone: Optional[str]
    mobile: Optional[str]
    lng: Optional[str]
    lat: Optional[str]


class AddressList(BaseModel):
    addresses: List[AddressItem]


class AddressRetrieve(BaseModel):
    address: AddressItem


class AddressFormItem(BaseModel):
    required: List[str]
    optional: List[str]
    regions: Dict[str, int]


class AddressFormRetrieve(BaseModel):
    address_form: AddressFormItem


class LineItem(BaseModel):
    name: str
    quantity: int
    price: float
    image: Optional[AnyHttpUrl]
    sku_id: Optional[int]
    product_id: Optional[int]
    category_id: Optional[int]


class OrderItem(BaseModel):
    date: datetime.datetime
    product_cost: Optional[float]
    shipping_cost: float
    total_cost: float
    line_items: List[LineItem]
    shop_id: int
    order_code: str


class SavedOdersList(BaseModel):
    saved_orders: Optional[List[OrderItem]]
