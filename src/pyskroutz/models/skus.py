import datetime

from .base import *
from typing import Optional


class SkuResponseModel(
    ItemBaseResponseModel, ItemBuyBaseResponseModel, WebUriResponseModel
):
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
    images: ItemImageBaseResponseModel
    favorited: Optional[bool]
    comparable: Optional[bool]
    name_source: Optional[str]


class SkuListResponseModel(BaseModel):
    skus: List[SkuResponseModel]
    meta: MetaResponseModel


class SkuRetrieveResponseModel(BaseModel):
    sku: SkuResponseModel


class SentimentResponseBody(BaseModel):
    positive: List[str]
    mediocre: List[str]


class ReviewResponseModel(BaseModel):
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
    sentiments: SentimentResponseBody


class ReviewListResponseModel(BaseModel):
    reviews: List[ReviewResponseModel]
    meta: MetaResponseModel


class SkuReviewVoteResponseModel(BaseModel):
    id: int
    sku_review_id: int
    user_id: int
    helpful: bool
    created_at: datetime.datetime


class SkuReviewVoteRetrieveResponseBody(BaseModel):
    sku_review_vote: SkuReviewVoteResponseModel


class SkuReviewFlagResponseModel(BaseModel):
    id: int
    flaggable_id: int
    flaggable_type: str
    user_id: int
    reason: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class AnswerResponseModel(BaseModel):
    id: int
    text: str


class QuestionResponseModel(BaseModel):
    text: str
    type: str
    answers: List[AnswerResponseModel]


class ReviewFormResponseModel(BaseModel):
    requires_body: bool
    questions: List[QuestionResponseModel]


class SkuReviewFormRetrieveResponseModel(BaseModel):
    review_form: ReviewFormResponseModel
