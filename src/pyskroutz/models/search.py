"""Response models for search
"""
from typing import List, Optional

from pydantic import BaseModel, AnyHttpUrl

from .base import (
    PaginationItem,
)
from .manufacturers import ManufacturerItem
from .skus import SkuItem


class AlternativeItem(BaseModel):
    term: str
    important: bool


class StrongMatcheItem(BaseModel):
    sku: Optional[SkuItem]
    manufacturer: Optional[ManufacturerItem]


class SearchMeta(BaseModel):
    q: Optional[str]
    alternatives: Optional[List[AlternativeItem]]
    strong_matches: Optional[StrongMatcheItem]
    pagination: Optional[PaginationItem]


class SearchResultCategoryItem(BaseModel):
    id: str
    name: str
    children_count: int
    image_url: AnyHttpUrl
    parent_id: int
    fashion: bool
    layout_mode: str
    web_uri: AnyHttpUrl
    code: str
    path: str
    show_specifications: bool
    manufacturer_title: str
    match_count: Optional[int]


class SearchResultsList(BaseModel):
    categories: Optional[List[SearchResultCategoryItem]]
    meta: SearchMeta


class AutocompleteItem(BaseModel):
    k: str
    i: int
    d: Optional[dict]


class AutocompleteList(BaseModel):
    autocomplete: Optional[List[AutocompleteItem]]
