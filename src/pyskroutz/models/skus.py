"""Response models for SKUs resources
"""
import datetime

from .base import *


class SkuItem(ItemBase, BuyableItemBase, WebUriBaseItem):
    ean: Optional[str]
    pn: Optional[str]
    display_name: str
    category_id: int
    first_product_shop_info: Optional[str]
    click_url: Optional[HttpUrl]
    plain_spec_summary: Optional[str]
    manufacturer_id: Optional[int]
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
    demoted: Optional[bool]
    votes_count: Optional[int]
    helpful_votes_count: Optional[int]
    voted: Optional[bool]
    flagged: Optional[bool]
    helpful: Optional[bool]
    sentiments: Optional[SentimentItem]


class ReviewList(BaseModel):
    reviews: Optional[List[ReviewItem]]
    meta: MetaItemBase


class VoteItem(BaseModel):
    id: int
    sku_review_id: int
    user_id: int
    helpful: bool
    created_at: datetime.datetime
    sku_review: Optional[ReviewItem]


class VoteRetrieve(BaseModel):
    sku_review_vote: Optional[VoteItem]


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
