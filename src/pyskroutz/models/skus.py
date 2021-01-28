import datetime

from .base import *
from typing import Optional


class SkuItem(ItemBase, BuyableItemBase, WebUriBaseItem):
    ean: str
    pn: str
    display_name: str
    category_id: int
    first_product_shop_info: Optional[str]
    click_url: Optional[HttpUrl]
    plain_spec_summary: str
    manufacturer_id: int
    future: bool
    virtual: bool
    images: ImageItemBase
    favorited: Optional[bool]
    comparable: Optional[bool]
    name_source: Optional[str]


class SkuList(BaseModel):
    skus: List[SkuItem]
    meta: MetaItemBase
    available_filters: Optional[AvailabilityFilterItem]


class SkuRetrieve(BaseModel):
    sku: SkuItem


class SentimentItem(BaseModel):
    positive: Optional[List[str]]
    mediocre: Optional[List[str]]


class ReviewItem(BaseModel):
    id: int
    user_id: int
    review: str
    rating: int
    created_at: datetime.datetime
    demoted: bool
    votes_count: int
    helpful_votes_count: int
    voted: bool
    flagged: bool
    helpful: bool
    sentiments: Optional[SentimentItem]


class ReviewList(BaseModel):
    reviews: List[ReviewItem]
    meta: MetaItemBase


class VoteItem(BaseModel):
    id: int
    sku_review_id: int
    user_id: int
    helpful: bool
    created_at: datetime.datetime
    sku_review: Optional[ReviewItem]


class VoteRetrieve(BaseModel):
    sku_review_vote: VoteItem


class FlagItem(BaseModel):
    id: int
    flaggable_id: int
    flaggable_type: str
    user_id: int
    reason: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class FlagRetrieve(BaseModel):
    flag: FlagItem


class AnswerItem(BaseModel):
    id: int
    text: str


class QuestionItem(BaseModel):
    text: str
    type: str
    answers: List[AnswerItem]


class ReviewFormItem(BaseModel):
    requires_body: bool
    questions: List[QuestionItem]


class ReviewFormRetrieve(BaseModel):
    review_form: ReviewFormItem
